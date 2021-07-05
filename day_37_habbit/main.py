import requests
import re
import json
from util.password_generator import TextGenerator
import pixe
import datetime
from util.patterns import Patterns

BASE_URL = "https://pixe.la"
VERSION = "v1"
USER_ENDPOINT = "users"
GRAPH_ENDPOINT = "graphs"
GRAPH_DEF_ENDPOINT = "graph-def"

PATTERN_TOKEN = "[ -~]{8,128}"
PATTERN_USERNAME = "[a-z][a-z0-9-]{1,32}"
PATTERN_GRAPH_ID = "[a-z][a-z0-9-]{1,16}"
PATTERN_INT = "^-?[0-9]+"
PATTERN_FLOAT = "^-?[0-9]+.[0-9]+"
TOKEN = "TmxUCeAB"
USERNAME = "kpl3"


def get_create_user_url() -> str:
    return "/".join([BASE_URL, VERSION, USER_ENDPOINT])


def get_graph_defs_url(username: str) -> str:
    return "/".join([get_create_user_url(), f"{username}", GRAPH_ENDPOINT])


def get_graph_id_url(username: str, graph_id: str) -> str:
    return "/".join([get_graph_defs_url(username), graph_id])


def get_graph_def_url(username: str, graph_id: str) -> str:
    return "/".join([get_graph_id_url(username, graph_id), GRAPH_DEF_ENDPOINT])


def get_update_pixel_url(username: str, graph_id:str, yyyyMMdd: str):
    return "/".join([get_graph_id_url(username, graph_id), yyyyMMdd])

def create_user(token: str, username: str, agree_terms_of_service: str = "yes",
                not_minor: str = "yes", thanks_code: str = None):
    token_match = re.match(PATTERN_TOKEN, token)
    if token_match is None:
        raise ValueError(f"Token: {token} does not match {PATTERN_TOKEN}")

    username_match = re.match(PATTERN_USERNAME, username)
    if username_match is None:
        raise ValueError(f"Username: {username} does not match {PATTERN_USERNAME}")

    body = {"token": token,
            "username": username,
            "agreeTermsOfService": agree_terms_of_service,
            "notMinor": not_minor}
    if thanks_code:
        body["thanksCode"] = thanks_code
    response = requests.post(get_create_user_url(), json=body)
    if response.raise_for_status() == requests.HTTPError:
        raise ConnectionError(f"create_user: {response.content}")
    return response.json()


def check_if_user_exist(username: str) -> bool:
    try:
        response = requests.get("/".join([BASE_URL, f"@{username}"]))
        _ = response.json()
    except requests.HTTPError:
        return False
    except json.JSONDecodeError:
        return True
    return True


def get_graph_defs(username: str, token: str):
    url = get_graph_defs_url(username)
    params = {"X-USER-TOKEN": token}
    response = requests.get(url, headers=params)
    print(f"get_graph_def: {response.content}")


def get_graph_def(username: str, token: str, graph_id: str):
    url = get_graph_def_url(username, graph_id)
    print(url)
    headers = {"X-USER-TOKEN": token}
    try:
        response = requests.get(url, headers=headers)
        resp_json = response.json()
    except requests.HTTPError as e:
        print(f"HTTPError (get_graph_def): {e}")
    except json.JSONDecodeError:
        raise ValueError(f"{response.content}")
    else:
        return resp_json


def create_graph(graph_id: str, graph_name: str, unit: str,
                 username: str, token: str,
                 color: pixe.PixeColor = pixe.PixeColor.GREEN,
                 unit_type: pixe.PixeUnitType = pixe.PixeUnitType.INT):

    # graph_id_match = re.match(PATTERN_GRAPH_ID, graph_id)
    # print(graph_id_match.span()[1])
    # if graph_id_match is None or graph_id_match.span()[1] < len(graph_id) - 1:
    #     raise ValueError(f"create_graph: graph_id not matching {PATTERN_GRAPH_ID}")

    Patterns.match(PATTERN_GRAPH_ID, graph_id, "create_graph")

    url = get_graph_defs_url(username)
    body = {"id": graph_id,
            "name": graph_name,
            "unit": unit,
            "type": unit_type.value,
            "color": color.value}
    headers = {"X-USER-TOKEN": token}

    try:
        response = requests.post(url, json=body, headers=headers)
    except requests.HTTPError as e:
        raise requests.HTTPError(f"create_graph: {e}")
    else:
        resp_json = response.json()
        if not resp_json["isSuccess"]:
            return None

        return response.json()


def get_graph_stats(username: str, graph_id: str):
    url = "/".join([get_graph_def_url(username), graph_id, "stats"])
    try:
        response = requests.get(url)
    except requests.HTTPError as e:
        return None
    else:
        return response.json()


def post_pixela(username: str, graph_id: str, token: str,
                quantity, date: datetime.date = datetime.date.today()) -> dict:
    definition = get_graph_def(username, token, graph_id)
    graph_unit_type = definition["type"]

    pattern = PATTERN_INT
    if graph_unit_type == pixe.PixeUnitType.FLOAT.value:
        pattern = PATTERN_FLOAT

    # quantity_match = re.match(pattern, f"{quantity}")
    # if quantity_match is None or quantity_match.span()[1] < len(f"{quantity}") - 1:
    #     raise ValueError(f"post_pixela: {quantity} does not match {pattern}")

    Patterns.match(pattern, f"{quantity}", "post_pixela")

    headers = {"X-USER-TOKEN": token}
    # formatted_date = "%04d%02d%02d" % (date.year, date.month, date.day)
    formatted_date = date.strftime("%Y%m%d")
    body = {"date": formatted_date, "quantity": f"{quantity}"}

    url = get_graph_id_url(username, graph_id)

    try:
        response = requests.post(url, json=body, headers=headers)
        resp_json = response.json()
    except requests.HTTPError as e:
        raise requests.HTTPError(f"post_pixela: {e}")
    except json.JSONDecodeError as e:
        print("post_pixela: JSONDecodeError")
        raise json.JSONDecodeError(f"{response.content}")
    else:
        return resp_json


def update_pixel(username: str, graph_id: str, date: datetime.date, token: str, quantity: str) -> bool:
    definition = get_graph_def(username, token, graph_id)
    graph_unit_type = definition["type"]

    pattern = PATTERN_INT
    if graph_unit_type == pixe.PixeUnitType.FLOAT.value:
        pattern = PATTERN_FLOAT

    Patterns.match(pattern, f"{quantity}", "post_pixela")

    url = get_update_pixel_url(username, graph_id, date.strftime("%Y%m%d"))
    headers = {"X-USER-TOKEN": token}
    body = {"quantity": quantity}
    try:
        response = requests.put(url, json=body, headers=headers)
        resp_json = response.json()
    except requests.HTTPError as e:
        print(f"update_pixel: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"update_pixel: {e}")
        return False
    else:
        print(resp_json)
        return resp_json["isSuccess"]


def delete_pixel(username: str, graph_id: str, date: datetime.date, token: str) -> bool:

    url = get_update_pixel_url(username, graph_id, date.strftime("%Y%m%d"))
    headers = {"X-USER-TOKEN": token}
    try:
        response = requests.delete(url, headers=headers)
        resp_json = response.json()
    except requests.HTTPError as e:
        print(f"delete_pixel: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"delete_pixel: {e}")
        return False
    else:
        print(resp_json)
        return resp_json["isSuccess"]


if not check_if_user_exist(USERNAME):
    create_user_response = create_user(
        token=TOKEN,
        username=USERNAME)
    if not create_user_response["isSuccess"]:
        raise ConnectionError(f"create_user_response: {create_user_response['message']}")

graph_id_name = "test-graph"

create_graph_resp = create_graph(graph_id=graph_id_name, graph_name=graph_id_name, unit="cm",
                                 unit_type=pixe.PixeUnitType.FLOAT, username=USERNAME, token=TOKEN)


get_graph_defs(USERNAME, TOKEN)

# unit_type = get_graph_def(USERNAME, TOKEN, graph_id_name)["type"]
# if unit_type == pixe.PixeUnitType.FLOAT.value:
#     unit_type = pixe.PixeUnitType.FLOAT
# else:
#     unit_type = pixe.PixeUnitType.INT

date = datetime.date.fromisoformat("2021-07-02")

print(post_pixela(USERNAME, graph_id_name, TOKEN, 10.10))

print(update_pixel(USERNAME, graph_id_name, date, TOKEN, "1.00"))

print(delete_pixel(USERNAME, graph_id_name, date, TOKEN))

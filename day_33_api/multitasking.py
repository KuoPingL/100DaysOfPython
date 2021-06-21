import requests
import threading


def long_running_process(tag=0):

    print(threading.currentThread().getName(), f"TAG {tag} Starting")
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    if response.status_code != 200:
        raise Exception(f"Bad response from ISS API : {response.status_code}")
    if response.raise_for_status() == requests.HTTPError:
        raise Exception(f"Bad response from ISS API : {response.status_code}")
    print(threading.currentThread().getName(), f"TAG {tag} Exiting")


for i in range(0, 5):
    long_running_process(i)


def long_running_processes():

    print(threading.currentThread().getName(), "Starting")
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    if response.status_code != 200:
        raise Exception(f"Bad response from ISS API : {response.status_code}")
    if response.raise_for_status() == requests.HTTPError:
        raise Exception(f"Bad response from ISS API : {response.status_code}")
    print(threading.currentThread().getName(), "Exiting")


for i in range(0, 5):
    w = threading.Thread(name=f"TAG{i}", target=long_running_processes)
    w.start()
    w.join()

import os
import requests
import datetime
import time

STOCK = "TSLA"
GRV_STOCK = "GPV.TRV"
COMPANY_NAME = "Tesla Inc"
GRV_COMPANY_NAME = "GPV.TRV"

CLOSE_KEY = "4. close"

STOCK_BASE_URL = "https://www.alphavantage.co/"
NEWS_URL_EVERYTHING = "https://newsapi.org/v2/everything"


def get_query(function: str) -> str:
    return STOCK_BASE_URL + f"query?function={function.upper()}"


def query_time_series_daily(symbol: str) -> dict:
    url = get_query("TIME_SERIES_DAILY") + f"&symbol={symbol}&apikey={os.getenv(symbol)}"
    response = requests.get(url)

    if response.raise_for_status() == requests.HTTPError:
        raise ConnectionError(f"Connection Error : {response}")

    return response.json()["Time Series (Daily)"]


def get_percentage_changes(input_json: dict, early_date: datetime.date, later_date: datetime.date) -> (datetime.date, datetime.date, float):

    if early_date > later_date:
        temp = early_date
        early_date = later_date
        later_date = temp

    assert later_date > early_date, "early_date should be earlier than later_date"

    while early_date.isoformat() not in input_json or \
            later_date.isoformat() not in input_json:
        if later_date.isoformat() not in input_json:
            later_date = later_date - datetime.timedelta(days=1)
        early_date = early_date - datetime.timedelta(days=1)

    early_day_price = float(input_json[early_date.isoformat()][CLOSE_KEY])
    later_day_price = float(input_json[later_date.isoformat()][CLOSE_KEY])

    return (early_date,
            later_date,
            (later_day_price - early_day_price) / later_day_price * 100)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
json = query_time_series_daily(GRV_STOCK)
yesterday = datetime.date.today() - datetime.timedelta(days=1) # datetime.date.fromisoformat("2021-06-30")#
day_before_yesterday = yesterday - datetime.timedelta(days=1) # datetime.date.fromisoformat("2021-05-06")# yesterday - datetime.timedelta(days=1)
day_before_yesterday, yesterday, percentage_difference = get_percentage_changes(json, early_date=yesterday,
                                                                                later_date=day_before_yesterday)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def search_news(title_keyword: str, from_date: str, to_date: str):
    url = NEWS_URL_EVERYTHING + f"?qInTitle={title_keyword}&from={from_date}&to={to_date}"
    response = requests.get(url=url, headers={'X-Api-Key': os.getenv("NEWS_API")})
    if response.raise_for_status() == requests.HTTPError:
        raise ConnectionError(f"Connection Error (search_news): {response.json()}")
    all_articles = response.json()["articles"]
    destine_index = 2
    if len(all_articles) <= 3:
        if len(all_articles) == 0:
            return None
        destine_index = len(all_articles)
    return all_articles[:destine_index]


def send_info(stock: str, percentage: float, headline: str, brief: str):
    from twilio.rest import Client
    account_sid = os.getenv("OWM_API_KEY")
    auth_token = os.getenv("OWM_AUTH_TOKEN")

    client = Client(account_sid, auth_token)
    icon = "🔺"
    if percentage < 0:
        icon = "🔻"

    client.messages.create(
        body=f"{stock}: {icon}{abs(int(percentage))}%\nHeadline: {headline}\nBrief: {brief}",
        from_='+13607955332',
        to='+8860918756081')


if percentage_difference >= 5 or percentage_difference <= -5:
    articles = search_news(GRV_COMPANY_NAME, from_date=day_before_yesterday.isoformat(), to_date=yesterday.isoformat())
    if articles:
        send_info(stock=GRV_STOCK, percentage=percentage_difference,
                  headline=articles[0]["title"], brief=articles[0]["description"])


# search_news(COMPANY_NAME, from_date=day_before_yesterday.isoformat(), to_date=yesterday.isoformat())


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


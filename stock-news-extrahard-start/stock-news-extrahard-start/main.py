import requests
import os
from twilio.rest import Client
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "UF4B3F6Z79LJEYYD"
NEWS_API_KEY = "e6da8f9ee248410686d1ea5da8ed9ef0"
account_sid = "AC1d16cd6bc0bcb27223af3e0c029f03c7"
auth_token = "1be827d8cd80bb8d4124748deeed36bc"

# STEP 1: Use https://www.alphavantage.com
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

endpoint = f'https://www.alphavantage.co/query'
response = requests.get(endpoint, params=params)
stock_data = response.json()["Time Series (Daily)"]

stocks_closed = [stock_data[key]["4. close"] for key in stock_data.keys()]

yest = float(stocks_closed[0])
before_yest = float(stocks_closed[1])
change = (yest - before_yest) / before_yest * 100
if change > 0:
    sign = "🔺" + str(round(change)) + "%"
else:
    sign = "🔻" + str(round(-1 * change)) + "%"
news_response = requests.get(
    url=f"https://newsapi.org/v2/everything?qInTitle={COMPANY_NAME}&from={date.today() - timedelta(days=1)}&sortBy"
        f"=publishedAt&apiKey={NEWS_API_KEY}&language=en")
articles = news_response.json()["articles"][:3]
message = f"News Alert. Keep informed with the changes in the stock market!\nTSLA:{sign}"
if change <= -5 or change >= 5:
    for item in articles:
        message += f"\nHeadline: {item['title']}\nBrief: {item['content']}"
    is_news = True
else:
    is_news = False

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#
#
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if is_news:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=message, from_="+15073534477", to='+233 55 340 5536')

    print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

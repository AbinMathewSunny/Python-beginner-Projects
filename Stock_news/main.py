import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_api_key = "2F5EO8HQA2W7E89C"
news_api_key = "5025950f987e4209ae7e204dc5344d61"
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : stock_api_key

}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
diff_percent = (difference/float(yesterday_closing_price)) * 100




    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if diff_percent > 0:
    news_params ={
        "apiKey":news_api_key,
        "qInTitle":COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]




    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

formatted_articles = [f"Headline:{article['title']}.\nBrief:{article['description']}" for article in three_articles]


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


my_email = os.getenv("my_email")
password = os.getenv("password")
connection = smtplib.SMTP("smtp.gmail.com", port=587)

connection.starttls()
connection.login(user=my_email,password=password)
for article in formatted_articles:
    subject = "Latest Tesla News Update"
    msg = f"Subject: {subject}\n\n{article}"
    msg = msg.encode("utf-8")
    connection.sendmail(from_addr=my_email,to_addrs=my_email,
                            msg=msg)
connection.close()

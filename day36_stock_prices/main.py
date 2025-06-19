import requests
from datetime import datetime, timedelta
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
C_NAME="apple"
Y_API_KEY= 
N_API = 
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey":"Y_API_KEY",
}
param={ 
    "q" : C_NAME,
    "from": "2025-04-29",
    "to": "2025-04-29",
    "sortBy": "popularity",
    "apiKey": 
}
response = requests.get(STOCK_ENDPOINT, params=PARAMETERS)
response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
data = response.json()
#print(data)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
today = datetime.now()
yesterday = today - timedelta(days=1)
daybfr_yday = today - timedelta(days=2)
print("Yesterday's date:", yesterday.strftime("%Y-%m-%d"))

y_stck_price= data["Time Series (Daily)"][yesterday.strftime("%Y-%m-%d")]["4. close"]
print("Yesterday's closing stock price $ :", y_stck_price)
#yesterday_date = yesterday.strftime("%Y-%m-%d")
#TODO 2. - Get the day before yesterday's closing stock price
print("Day before yesterday's date:", daybfr_yday.strftime("%Y-%m-%d"))
d_stck_price= data["Time Series (Daily)"][daybfr_yday.strftime("%Y-%m-%d")]["4. close"]
print("Day before yesterday's closing stock price-  $ :", d_stck_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff= abs(float(y_stck_price) - float(d_stck_price))
print("Difference in stock price $ :", diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
print("Percentage difference in stock price % :", (diff/float(d_stck_price))*100)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if (diff/float(d_stck_price))*100 > 1:
    response = requests.get(NEWS_ENDPOINT, params=param)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    data = response.json()
    articles = data["articles"]
    one_article = articles[:1]
    print(one_article)
else:
    print("The news is not that great, so no need to get news.")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


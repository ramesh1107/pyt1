#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import dotenv
import os
dotenv.load_dotenv()
from pprint import pprint
URL= os.getenv("URL1") 
UNM= os.getenv("UNM")
PWD= os.getenv("PWD")
auth1=(UNM, PWD)
#get request to get all the cities and prices
response= requests.get(
    url=URL,
    auth= auth1
)
response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
data = response.json()
pprint(data)
#Post request to add a new city with price
pr=requests.post(
    url=URL,
    json={
        "price": {
            "city": "banhalore", 
            "iataCode": "344",
            "lowestPrice": 1000
        }
    },
    auth=(auth1)
)
response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
pr_data= pr.json()
pprint(pr_data) 
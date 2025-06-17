import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
SMTP_ADDRESS= os.getenv("SMTP_ADDRESS")
#SMTP_PORT= os.getenv("SMTP_PORT")   
My_EMAIL = os.getenv("My_EMAIL")
My_PASSWORD = os.getenv("My_PASSWORD")

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8"
}

pURL="https://appbrewery.github.io/instant_pot/"
URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(URL, headers=header)
#print(response.status_code) 


soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())
#price=soup.find(class_="a-offscreen ").get_Text()
price = soup.find(class_="a-offscreen").get_text()
pwd= price.split("$")[1]

pwd_af=float(pwd)
print(pwd_af)

if pwd_af < 100:
    print("Price is less than 100")
    connection= smtplib.SMTP(SMTP_ADDRESS, 587)
    connection.starttls()
    connection.login(user=My_EMAIL, password=My_PASSWORD)
    connection.sendmail(from_addr=My_EMAIL, to_addrs=My_EMAIL, 
                        msg="Subject:Amazon Price Alert!\n\nThe price of the Instant Pot is now below $100! Check it out here: https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
else:
    print("Sorry the Price is more than 100")
    connection= smtplib.SMTP(SMTP_ADDRESS, 587)
    connection.starttls()
    connection.login(user=My_EMAIL, password=My_PASSWORD)
    connection.sendmail(from_addr=My_EMAIL, to_addrs=My_EMAIL, 
                        msg="Subject:Wait dont buy!\n\nThe price is too high !")




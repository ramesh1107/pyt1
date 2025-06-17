import requests
import urllib.parse
import smtplib
from datetime import datetime#df is your dataframe with a datetime column

My_EMAIL = "testingpytester1@gmail.com"
My_PASSWORD ="dleg uhoe gywp zcyv"
My_LAT = (12.9716 -5)
My_LNG = (77.5946-5)

url= "https://api.sunrise-sunset.org/json?lat={}&lng={}".format(My_LAT, My_LNG)
#print (url)
def is_iss_aboveyou():

    response = requests.get(url ="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    #if response.status_code == 200:
    data = response.json()["iss_position"]
    iss_lat = float(data["latitude"])
    iss_lng = float(data["longitude"])
    if iss_lat < My_LAT and iss_lng < My_LNG:
       return True
    else:
        return False
def is_night():
    response= requests.get(url = url)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    data = response.json()
    sunrise = int(data["results"]["sunrise"])
    sunset = int(data["results"]["sunset"])
    time_now= datetime.now()
    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False
if is_iss_aboveyou() and is_night():
    print("The ISS is above you and it's night time!")
    connection= smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=My_EMAIL, password=My_PASSWORD)
    connection.sendmail(from_addr=My_EMAIL, to_addrs=My_EMAIL, 
                        msg="Subject:Look Up!\n\nThe ISS is above you in the sky!")
else:
    print("The ISS is not above you or it's not night time.")
    connection= smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=My_EMAIL, password=My_PASSWORD)
    connection.sendmail(from_addr=My_EMAIL, to_addrs=My_EMAIL, 
                        msg="Subject:Look Up!\n\nThe ISS is not above you in the sky!")

'''elif response.status_code == 404:
    print("Error:", response.status_code)
elif response.status_code == 401:
    print("Error:", response.status_code)
parm ={"lat": My_LAT,
        "lng": My_LNG,
        "formatted": 0,}
#response = requests.get(url ="https://api.sunrise-senset.org/json", params=parm)
response= requests.get(url = url)
response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
if response.status_code == 200:
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    print("Sunrise:", sunrise)
    print("Sunset:", sunset)
    time_now = datetime.now()
    print("Current Time:", time_now.strftime("%H:%M:%S"))
elif response.status_code == 404:   
    print("Error:", response.status_code)
elif response.status_code == 401:
    print("Error:", response.status_code)'''

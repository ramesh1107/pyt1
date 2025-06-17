import requests
from datetime import datetime, timedelta

p_endpoint = "https://pixe.la/v1/users"
u_parms = {
    "token": "hsdkrisdaring34st30anal38",
    "username": "krisdarling",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"   

}
UNAME = "krisdarling"
TOKEN = "hsdkrisdaring34st30anal38"
GN= "graph1"
'''response= requests.post(url=p_endpoint, json=u_parms)
print(response.text)'''    
g_endpoint = f"{p_endpoint}/{UNAME}/graphs"
g_parms = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
hdr = {
    "X-USER-TOKEN": TOKEN
}
#resp= requests.post(url=g_endpoint, json=g_parms, headers=hdr)
#print(resp.text)    

#Posting a pixel
#https://pixe.la/v1/users/krisdarling/graphs/graph1
today = datetime.now()
p_endpoint = f"{p_endpoint}/{UNAME}/graphs/{GN}"
p_parms = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5",
}
resp1= requests.post(url=p_endpoint, json=p_parms, headers=hdr)
print(resp1.text)        

#PUT method 

#PUT https://pixe.la/@a-know -H 'X-USER-TOKEN:thisissecret' -d '{"displayName":"a-know"}'
#{"message":"Success.","isSuccess":true}
#PUT https://pixe.la/v1/users/krisdarling/graphs/graph1 -H 'X-USER-TOKEN:hsdkrisdaring34st30anal38' -d '{"name":"Cycling Graph","unit":"Km","type":"float","color":"ajisai"}'

upd_endpoint = f"{p_endpoint}/{UNAME}/graphs/{GN}/today.strftime('%Y%m%d')"
put_params = {
    "quantity": "34",
}
put_resp = requests.put(url=upd_endpoint, json=put_params, headers=hdr)
print(put_resp.text)

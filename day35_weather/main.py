import requests
O_ep="https://api.openweathermap.org/data/2.5/weather"
w_parameters={
    "lat":12.9716,
    "lon":77.5946,
    "appid":"c6f8dc8af455f3dfe99c49d97781ba6d",
    "cnt":4,
}
api_key="c6f8dc8af455f3dfe99c49d97781ba6d"
response=requests.get(url=O_ep, params=w_parameters)
#print(response.status_code)
print(response.json())
response.raise_for_status() 
weather_data=response.json()
weather_description=weather_data["weather"][0]["description"]
#print(weather_description)
temp= weather_data["main"]["temp"]
temp_min=weather_data["main"]["temp_min"]
temp_max=weather_data["main"]["temp_max"]   
temp_feel=weather_data["main"]["feels_like"]
temp_humidity=weather_data["main"]["humidity"]
temp_celcius=temp-273.15  
temp_min_celcius=temp_min-273.15
temp_max_celcius=temp_max-273.15  
temp_feel=temp_feel-273.15  
print(f"Weather description: {weather_description}")
print(f"Temperature in Celsius: {temp_celcius:.2f}°C")
print(f"Minimum Temperature in Celsius: {temp_min_celcius:.2f}°C")
print(f"Maximum Temperature in Celsius: {temp_max_celcius:.2f}°C")
print(f"Feels Like Temperature in Celsius: {temp_feel:.2f}°C")
print(f"Humidity: {temp_humidity}%")
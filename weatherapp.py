import requests 
import json
city = input("Enter a city name : ")
key= "b42f08800d882f5397e89d12fe889b2f"
URL = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}")

data =URL.json()


print("Temperature = ",data["main"]["temp"])

print("Humidity = ",data["main"]["humidity"])

print("Weather coditons = ",data["weather"])

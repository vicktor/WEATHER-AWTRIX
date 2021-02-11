#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json

headers = {
  'Content-Type': 'application/json'
}

url_ns = "https://api.openweathermap.org/data/2.5/weather?q=Barcelona,es&appid=your_api_key&units=metric&lang=en"


response = requests.request("GET", url_ns, headers=headers)

print(response.json())

description = response.json()['weather'][0]['description']
temp = response.json()['main']['temp']
humidity = response.json()['main']['humidity']
wind = response.json()['wind']['speed']

payload='{{"name":"WEATHERNotification", "force":true, "repeat":1,"scrollSpeed": 80, "icon":433, "moveIcon":false, "multiColorText":[{{"text":"{description}  ",
"color":[80,110,255]}},{{"text":"temp: {temp}","color":[0,255,0]}}, {{"text":"ºC  Humidity: {humidity}  wind: {wind}    ","color":[80,110,255]}}], "color":[80,1
10,255]}}'

payload = payload.format(description=description, temp=temp, humidity=humidity, wind=wind)

url = "http://192.168.1.110:7000/api/v3/notify"

response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))

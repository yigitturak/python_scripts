import json
import requests

api_key="20c95ff2c47c2aaa616889e940df9509"
city="Amsterdam"
url="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

req = requests.get(url)
json = req.json()
print(json)

desc = json.get("weather")[0].get("description")
print("The weather is " + desc)

temp_min=json.get("main").get("temp_min")
temp_max=json.get("main").get("temp_max")
temp = json.get("main").get("temp")

print("Today min temp is",temp_min,"\ntemp max is",temp_max,"\ntemp is",temp)

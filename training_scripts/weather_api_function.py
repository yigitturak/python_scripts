import json
import requests

def get_today_weather():
    api_key="20c95ff2c47c2aaa616889e940df9509"
    city="Amsterdam"
    url="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"
    req = requests.get(url)
    json = req.json()
    desc = json.get("weather")[0].get("description")

    temp_min=json.get("main").get("temp_min")
    temp_max=json.get("main").get("temp_max")
    temp = json.get("main").get("temp")

    return {'description': desc,
    'temp_min':temp_min,
    'temp_max':temp_max,
    'temp':temp}

def main():
    weather_dict=get_today_weather()
    print("The weather is " + weather_dict.get('description'))

    print("Today min temp is",weather_dict.get('temp_min'),"\ntemp max is",weather_dict.get('temp_max'),"\ntemp is",weather_dict.get('temp'))

main()
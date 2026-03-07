#Get your API from openweathermap.org
from datetime import datetime
import requests
import json

api_key ='683bfea10bb8447e874133229260503'
city = input("Enter your city name : ")
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)
data = response.json()
status = response.status_code #200 = success.

if(status==200):
    try:
        now = datetime.now()
        time = now.strftime("%A %d %B %Y")
        print(f'\nThe weather of "{time}" is given below.')
        print(f'{data["location"]["name"]}/{data["location"]["country"]}')
        print(f'Temprature : {data["current"]["temp_c"]}°C (Feelslike {data["current"]["feelslike_c"]}°C)')
        print(f'Condition : {data["current"]["condition"]["text"]}')
        print(f'Raining chance: {data["current"]["precip_mm"]}%')
        print(f'Humidity : {data["current"]["humidity"]} \nWind speed : {data["current"]["wind_kph"]}Kmh.')
    except KeyError:
        print(f"No location found with name '{city}'")
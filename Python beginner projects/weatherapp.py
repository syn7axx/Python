from datetime import datetime
import requests

api_key = 'Enter_Your_Key_Here' #get your api from weatherapi.com
city = input("Enter your city name: ")
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

try:
    response = requests.get(url, timeout=10)
    status = response.status_code
    data = response.json()
except requests.exceptions.RequestException:
    print("Please check your internet connection.")
    exit()
except ValueError:
    print("Error decoding response.")
    exit()

if status == 401:
    print("Invalid API key. Enter a correct key.")
    exit()
elif status != 200:
    print(f"Error fetching data. Status code: {status}")
    exit()

try:
    now = datetime.now()
    time = now.strftime("%A %d %B %Y")
    location = f'{data["location"]["name"]}, {data["location"]["country"]}'
    temp = f'{data["current"]["temp_c"]}°C (Feels like {data["current"]["feelslike_c"]}°C)'
    condition = data["current"]["condition"]["text"]
    precip = f'{data["current"]["precip_mm"]} mm'
    humidity = f'{data["current"]["humidity"]}%'
    wind = f'{data["current"]["wind_kph"]} km/h'

    print(f'\nWeather for "{time}" in {location}:')
    print(f'Temperature: {temp}')
    print(f'Condition: {condition}')
    print(f'Precipitation: {precip}')
    print(f'Humidity: {humidity}')
    print(f'Wind speed: {wind}')
except KeyError:
    print(f"No location found with name '{city}'")

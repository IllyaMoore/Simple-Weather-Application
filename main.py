from GetTodaysWeather import get_weather_by_day
from GetWeakWeather import get_weather_by_week
import requests
from datetime import date
from API import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

today_date = date.today()
choice = input("placeholder: ")
city = input("Imput city: ")
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if choice == "1":
    get_weather_by_day(city, response, today_date)
elif choice == "2":
    get_weather_by_week(city, response, today_date) 
else: 
    print("1 or 2")



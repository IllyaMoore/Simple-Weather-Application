from GetTodaysWeather import get_weather_by_day
from GetWeakWeather import get_weather_by_week
import requests
from datetime import date, timedelta
from API import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

today_date = date.today()

choice = input("Choose an option: \n 1.Weather on tomorrows day.\n 2.Weather on next 5 days\n")


city = input("Imput city: ")
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if choice == "1":
    print("\nHire is your result:")
    get_weather_by_day(city, response, today_date)
elif choice == "2":
    print("\nHire is your results:")
    get_weather_by_week(city, response, today_date) 
else: 
    print("We only have two options at the moment, please choose from them")



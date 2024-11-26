
def get_weather_by_day(city, response, today_date):
    if response.status_code == 200:
        data = response.json()
        print("Todays weather: ")
        print(f"On date: {today_date}")
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Wind speed: {data['wind']['speed']} m/s")
    else:
        print(f"Error: {response.status_code} - {response.text}")


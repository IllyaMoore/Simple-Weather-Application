from datetime import timedelta

def get_weather_by_week(city, response, today_date):
    for i in range(5):
        today_date = today_date + timedelta(days=1)
        if response.status_code == 200:
            data = response.json()
            print("\nWeather: ")
            print(f"On date: {today_date}")
            print(f"Weather in {city}: {data['weather'][0]['description']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Feels like: {data['main']['feels_like']}°C")
            print(f"Wind speed: {data['wind']['speed']} m/s\n")
        else:
            print(f"Error: {response.status_code} - {response.text}")


import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Load .env file (make sure it's named .env and in the same folder)
load_dotenv()

def get_weather(city_name):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        print("❌ API key is missing! Check your .env file and spelling.")
        return

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n📅 Date & Time:", now)
        print(f"🌍 Weather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"🥵 Feels Like: {data['main']['feels_like']}°C")
        print(f"🌤️ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🔽 Pressure: {data['main']['pressure']} hPa")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")

        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
        print(f"🌅 Sunrise: {sunrise}")
        print(f"🌇 Sunset: {sunset}")

        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        print(f"🖼️ Icon: {icon_url}\n")

    elif response.status_code == 404:
        print("❌ City not found! Please check the name.\n")
    else:
        print("❌ Failed to retrieve weather data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

# Main loop
while True:
    city = input("Enter a city (or 'exit' to quit): ")
    if city.lower() == 'exit':
        print("👋 Exiting weather app.")
        break
    get_weather(city)

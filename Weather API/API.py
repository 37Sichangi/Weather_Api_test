import requests
from dotenv import load_dotenv
import os

# Load .env file (make sure it's named .env and in same folder as this script)
load_dotenv()

def get_weather(city_name):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    # Debug: Print loaded API key
    print("Loaded API Key:", api_key)

    if not api_key:
        print("❌ API key is missing! Check your .env file and spelling.")
        return

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Debug: Print raw response
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        data = response.json()
        print(f"🌍 Weather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"🌤️ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("❌ Failed to retrieve weather data.")

# Ask user for city input
city = input("Enter a city: ")
get_weather(city)

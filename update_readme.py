import os
import re
import requests
from datetime import datetime
import pytz


# Your location coordinates (Modi'in, Israel)
LAT = "31.8940"
LON = "35.0132"

# Get API key from GitHub secrets
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

def get_weather():
    """Fetch current weather data"""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        # Get weather info
        temp = int(round(data["main"]["temp"]))  # Round to nearest degree
        description = data["weather"][0]["description"]
        
        # Get sunrise and sunset info (convert from Unix timestamp to local time)
        israel_tz = pytz.timezone('Asia/Jerusalem')
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"], tz=pytz.utc).astimezone(israel_tz)
        sunset = datetime.fromtimestamp(data["sys"]["sunset"], tz=pytz.utc).astimezone(israel_tz)
        
        sunrise_time = sunrise.strftime("%H:%M")
        sunset_time = sunset.strftime("%H:%M")
        
        return {
            "temp": temp,
            "description": description,
            "sunrise": sunrise_time,
            "sunset": sunset_time
        }
    
    return None

def update_readme():
    """Update the README with latest weather data"""
    # Get current weather
    weather = get_weather()
    if not weather:
        print("Failed to get weather data")
        return
    
    # Get current time in Israel
    israel_time = datetime.now(pytz.timezone('Asia/Jerusalem'))
    current_time = israel_time.strftime("%A, %d %B, %H:%M %Z")
    
    # Read the current README
    with open('README.md', 'r', encoding='utf-8') as file:
        readme = file.read()
    
    # Update weather information
    # Update temperature and description
    weather_pattern = r'Currently in Modi\'in: <b>.*?°C,\s*<i>.*?</i></b>'
    weather_replacement = f'Currently in Modi\'in: <b>{weather["temp"]}°C, <i>{weather["description"]}</i></b>'
    readme = re.sub(weather_pattern, weather_replacement, readme)
    
    # Update sunrise and sunset times
    sun_pattern = r'Today, the sun rises at <b>.*?</b> and sets at <b>.*?</b>'
    sun_replacement = f'Today, the sun rises at <b>{weather["sunrise"]}</b> and sets at <b>{weather["sunset"]}</b>'
    readme = re.sub(sun_pattern, sun_replacement, readme)
    
    # Update the last refresh time
    refresh_pattern = r'Last refresh: .*?<br>'
    refresh_replacement = f'Last refresh: {current_time}<br>'
    readme = re.sub(refresh_pattern, refresh_replacement, readme)
    
    # Write the updated content back to the README
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(readme)
    
    print("README updated successfully")

if __name__ == "__main__":
    update_readme()
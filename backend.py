import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    
    return filtered_data

# This condition checks of this get_data function is only triggered when we're executing
# the script directly, and not when the script is being imported from somewhere else

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, view="Sky"))
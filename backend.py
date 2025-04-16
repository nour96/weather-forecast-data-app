import requests

API_KEY = "882f231b3b1f01c244ea2ad3df5b786c"

def get_data(place, forecast_days=None, view=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    
    if view == "Temperature":
        filtered_data = [item["main"]["temp"] for item in filtered_data]
    if view == "Sky":
        filtered_data = [item["weather"][0]["main"] for item in filtered_data]
    return filtered_data

# This condition checks of this get_data function is only triggered when we're executing
# the script directly, and not when the script is being imported from somewhere else

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, view="Sky"))
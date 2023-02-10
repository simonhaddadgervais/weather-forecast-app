import requests

API_KEY = {OPEN_WEATHER_API_KEY}  # Get an API key from openweathermap.org


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    # get "list" from the API response
    filtered_data = data["list"]
    number = 8 * days
    filtered_data = filtered_data[:number]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Paris", days=3))


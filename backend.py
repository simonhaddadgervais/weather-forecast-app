import requests

API_KEY = API_KEY_WEATHER


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number = 8 * days
    filtered_data = filtered_data[:number]
    return filtered_data


if __name__ == "__main__":
    print(os.environ.get("API_KEY_WEATHER"))


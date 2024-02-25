import requests
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    header = {"authorization": PEXELS_API_KEY}
    params = {
        "query": city + " " + state,
        "per_page": 1
    }
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params=params, headers=header)
    content = response.json()

    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}

    except (KeyError, IndexError):
        return {"picture_url": None}


def get_weather(city, state):
    params = {
        "q": city + " " + state,
        "appid": OPEN_WEATHER_API_KEY,
        "limit": 1
    }
    url = "http://api.openweathermap.org/geo/1.0/direct"

    response = requests.get(url, params=params,)
    coordinates = response.json()

    weather_url = "https://api.openweathermap.org/data/2.5/weather"

    weather_params = {
        "lat": coordinates[0]["lat"],
        "lon": coordinates[0]["lon"],
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial"
    }

    weather_response = requests.get(weather_url, params=weather_params)

    local_weather = weather_response.json()

    try:
        return {
            "weather": {
                "description": local_weather["weather"][0]["description"],
                "temperature": local_weather["main"]["temp"]
            }
        }

    except (KeyError, IndexError):
        return {"weather": None}

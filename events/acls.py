import json
import requests
from .keys import PEXELS_API_KEY


def get_photo(city, state):
    header = {"authorization": PEXELS_API_KEY}
    params = {
        "query": city + " " + state,
        "per_page": 1
    }
    url = "https://api.pexels.com/v1/search"

    response = requests.get(url, params-params, headers=header)
    content = response.json()

    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}

    except (KeyError, IndexError):
        return {"picture_url": None}

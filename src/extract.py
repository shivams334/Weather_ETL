import os
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
CITIES = os.getenv("CITIES", "").split(",")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_city_weather(city: str) -> dict:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    data["fetched_at"] = datetime.now(timezone.utc).isoformat()
    return data

def extract_all() ->dict:
    results = []
    for city in CITIES:
        try:
            data = fetch_city_weather(city)
            print(f"[extract] Fetched: {city}")
            results.append(data)
        except Exception as e:
            print(f"[extract] Error fetching {city}: {e}")
    return results

if __name__ == "__main__":
    import json
    results = extract_all()
    print(json.dumps(results[0], indent=2))


import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from unittest.mock import patch, MagicMock
from extract import fetch_city_weather, extract_all

FAKE_API_RESPONSE = {
    "name": "London",
    "sys": {"country": "GB"},
    "main": {"temp": 18.5, "feels_like": 17.2, "humidity": 72},
    "wind": {"speed": 4.1},
    "weather": [{"description": "light rain"}],
    "dt": 1718700000,
}


def test_fetch_city_weather_returns_dict():
    with patch("extract.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = FAKE_API_RESPONSE
        mock_get.return_value = mock_response

        result = fetch_city_weather("London")

        assert isinstance(result, dict)
        assert result["name"] == "London"
        assert "fetched_at" in result


def test_extract_all_skips_failed_cities():
    with patch("extract.requests.get") as mock_get:
        mock_get.side_effect = Exception("API error")
        results = extract_all()
        assert results == []

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from transform import transform

FAKE_RAW = [
    {
        "name": "London",
        "sys": {"country": "GB"},
        "main": {"temp": 18.5, "feels_like": 17.2, "humidity": 72},
        "wind": {"speed": 4.1},
        "weather": [{"description": "light rain"}],
        "fetched_at": "2026-06-19T10:00:00+00:00",
    }
]


def test_transform_columns():
    df = transform(FAKE_RAW)
    expected_columns = [
        "city", "country", "temperature_c", "feels_like_c",
        "humidity_pct", "wind_speed_ms", "weather_desc", "fetched_at"
    ]
    assert list(df.columns) == expected_columns


def test_transform_values():
    df = transform(FAKE_RAW)
    assert df["city"][0] == "London"
    assert df["temperature_c"][0] == 18.5
    assert df["humidity_pct"][0] == 72


def test_transform_row_count():
    df = transform(FAKE_RAW)
    assert len(df) == 1

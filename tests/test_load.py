import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pandas as pd
from unittest.mock import patch, MagicMock
from load import get_connection, load

FAKE_DF = pd.DataFrame([{
    "city": "London",
    "country": "GB",
    "temperature_c": 18.5,
    "feels_like_c": 17.2,
    "humidity_pct": 72,
    "wind_speed_ms": 4.1,
    "weather_desc": "light rain",
    "fetched_at": "2026-06-19T10:00:00+00:00",
}])


def test_get_connection_called():
    with patch("load.psycopg2.connect") as mock_connect:
        get_connection()
        assert mock_connect.called


def test_load_commits_transaction():
    with patch("load.psycopg2.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        load(FAKE_DF)

        mock_conn.commit.assert_called_once()

CREATE TABLE IF NOT EXISTS weather_data (
    id              SERIAL PRIMARY KEY,
    city            VARCHAR(100)    NOT NULL,
    country         VARCHAR(10)     NOT NULL,
    temperature_c   NUMERIC(5, 2)   NOT NULL,
    feels_like_c    NUMERIC(5, 2),
    humidity_pct    INTEGER,
    wind_speed_ms   NUMERIC(6, 2),
    weather_desc    VARCHAR(200),
    fetched_at      TIMESTAMP       NOT NULL,
    created_at      TIMESTAMP       DEFAULT NOW()
);

CREATE UNIQUE INDEX IF NOT EXISTS uix_weather_city_hour
    ON weather_data (city, DATE_TRUNC('hour', fetched_at));


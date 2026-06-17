import pandas as pd

def transform(raw_records: list[dict]) -> pd.DataFrame:
    rows = []
    for record in raw_records:
        row = {
            "city":          record["name"],
            "country":       record["sys"]["country"],
            "temperature_c": record["main"]["temp"],
            "feels_like_c":  record["main"]["feels_like"],
            "humidity_pct":  record["main"]["humidity"],
            "wind_speed_ms": record["wind"]["speed"],
            "weather_desc":  record["weather"][0]["description"],
            "fetched_at":    record["fetched_at"],
        }
        rows.append(row)
    return pd.DataFrame(rows)

if __name__ == "__main__":
    from extract import extract_all
    raw = extract_all()
    df = transform(raw)
    print(df)



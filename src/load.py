import os 
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def load(df):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO weather_data
            (city, country, temperature_c, feels_like_c, humidity_pct, 
            wind_speed_ms, weather_desc, fetched_at)
        VALUES (%(city)s, %(country)s, %(temperature_c)s, %(feels_like_c)s, %(humidity_pct)s, 
            %(wind_speed_ms)s, %(weather_desc)s, %(fetched_at)s)
        ON CONFLICT DO NOTHING;
    """
    rows = df.to_dict(orient="records")
    cursor.executemany(sql, rows)
    conn.commit()
    cursor.close()
    conn.close()    
    print(f"[load] Inserted {len(rows)} records into the database.")
    

    
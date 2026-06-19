# Weather ETL Pipeline

A beginner-level data engineering project that extracts live weather data from the OpenWeatherMap API, transforms it using pandas, and loads it into a PostgreSQL database.

## What it does

- Fetches current weather data for multiple cities via the OpenWeatherMap API
- Cleans and flattens the raw JSON response into a structured table
- Inserts the data into PostgreSQL — safely ignoring duplicates if run multiple times in the same hour

## Tech Stack

- **Python 3.8+**
- **pandas** — data transformation
- **psycopg2** — PostgreSQL connection
- **requests** — HTTP API calls
- **python-dotenv** — environment variable management
- **pytest** — automated tests
- **Docker** — running PostgreSQL locally

## Project Structure

```
weather-etl/
├── src/
│   ├── extract.py      # Fetch data from OpenWeatherMap API
│   ├── transform.py    # Clean and flatten raw JSON
│   ├── load.py         # Insert data into PostgreSQL
│   └── pipeline.py     # Orchestrate all three steps
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── sql/
│   └── create_tables.sql   # PostgreSQL schema
├── .env.example            # Template for environment variables
└── requirements.txt
```

## Prerequisites

- Python 3.8 or higher
- Docker Desktop installed and running
- A free OpenWeatherMap API key — sign up at [openweathermap.org](https://openweathermap.org/api)

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd weather-etl
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Open `.env` and fill in:

```
API_KEY=your_openweathermap_api_key
CITIES=London,Mumbai,New York,Tokyo,Sydney

DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydb
DB_USER=admin
DB_PASSWORD=admin123
```

You can change the `CITIES` list to any cities you want — comma separated, no spaces around commas.

### 5. Start PostgreSQL with Docker

```bash
docker run --name weather_postgres \
  -e POSTGRES_DB=mydb \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin123 \
  -p 5432:5432 \
  -d postgres
```

If you already have the container and just need to start it:

```bash
docker start weather_postgres
```

### 6. Create the database table

```bash
docker exec -i weather_postgres psql -U admin -d mydb < sql/create_tables.sql
```

## Running the Pipeline

```bash
python src/pipeline.py
```

Expected output:

```
[pipeline] Starting...
[extract] Fetched: London
[extract] Fetched: Mumbai
[extract] Fetched: New York
[extract] Fetched: Tokyo
[extract] Fetched: Sydney
[load] Inserted 5 records into the database.
[pipeline] Done.
```

You can run it multiple times — duplicate records within the same hour are automatically ignored.

## Verifying the Data

Connect to PostgreSQL and query the table:

```bash
docker exec -it weather_postgres psql -U admin -d mydb -c "SELECT * FROM weather_data;"
```

## Running the Tests

```bash
python -m pytest tests/ -v
```

All 7 tests should pass. No internet connection or database required for tests — all external dependencies are mocked.

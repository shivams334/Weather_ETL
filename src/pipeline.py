from extract import extract_all
from transform import transform
from load import load

def run_pipeline():
    print("[pipeline] Starting...")
    raw_data = extract_all()
    clean_data = transform(raw_data)
    load(clean_data)

    print("[pipeline] Done.")


if __name__ == "__main__":
    run_pipeline()

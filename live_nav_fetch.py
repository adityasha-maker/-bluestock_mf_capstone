import requests
import pandas as pd
from pathlib import Path

RAW_PATH = Path(r"C:\Users\sharm\OneDrive\Desktop\DATASETS CSV")

schemes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            RAW_PATH / f"{name}_nav.csv",
            index=False
        )

        print(f"Saved {name}")

    except Exception as e:
        print(f"Error fetching {name}: {e}")

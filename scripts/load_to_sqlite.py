from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

RAW = Path(r"C:\Users\sharm\OneDrive\Desktop\DATASETS CSV")
PROCESSED = RAW / "processed"

DB_PATH = r"C:\Users\sharm\OneDrive\Desktop\bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

print("Loading datasets...")

fund_master = pd.read_csv(
    RAW / "01_fund_master.csv"
)

nav = pd.read_csv(
    PROCESSED / "clean_nav_history.csv"
)

txn = pd.read_csv(
    PROCESSED / "clean_investor_transactions.csv"
)

perf = pd.read_csv(
    PROCESSED / "clean_scheme_performance.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")
print("Location:", DB_PATH)
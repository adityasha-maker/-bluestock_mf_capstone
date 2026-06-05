import pandas as pd
from pathlib import Path

PROCESSED = Path(r"C:\Users\sharm\OneDrive\Desktop\DATASETS CSV\processed")

nav = pd.read_csv(PROCESSED / "clean_nav_history.csv")
txn = pd.read_csv(PROCESSED / "clean_investor_transactions.csv")
perf = pd.read_csv(PROCESSED / "clean_scheme_performance.csv")

print("="*60)
print("NAV DATA")
print("="*60)
print(nav.describe())

print("\n")

print("="*60)
print("TRANSACTION DATA")
print("="*60)
print(txn.describe())

print("\n")

print("="*60)
print("PERFORMANCE DATA")
print("="*60)
print(perf.describe())
print("\n" + "="*60)
print("CATEGORY DISTRIBUTION")
print("="*60)

print(
    perf["category"]
    .value_counts()
)

print("\n" + "="*60)
print("RISK DISTRIBUTION")
print("="*60)

print(
    perf["risk_grade"]
    .value_counts()
)

print("\n" + "="*60)
print("AVERAGE 3 YEAR RETURN BY CATEGORY")
print("="*60)

print(
    perf.groupby("category")["return_3yr_pct"]
    .mean()
    .sort_values(ascending=False)
)

print("\n" + "="*60)
print("AGE GROUP DISTRIBUTION")
print("="*60)

print(
    txn["age_group"]
    .value_counts()
)

print("\n" + "="*60)
print("GENDER DISTRIBUTION")
print("="*60)

print(
    txn["gender"]
    .value_counts()
)

print("\n" + "="*60)
print("TOP 10 STATES")
print("="*60)

print(
    txn["state"]
    .value_counts()
    .head(10)
)
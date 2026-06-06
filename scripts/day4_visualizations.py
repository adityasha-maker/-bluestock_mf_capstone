import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Paths
PROCESSED = Path(
    r"C:\Users\sharm\OneDrive\Desktop\DATASETS CSV\processed"
)

REPORTS = Path("reports")
REPORTS.mkdir(exist_ok=True)

# Load data
perf = pd.read_csv(
    PROCESSED / "clean_scheme_performance.csv"
)

txn = pd.read_csv(
    PROCESSED / "clean_investor_transactions.csv"
)

# --------------------------------------------------
# 1. Average 3-Year Return by Category
# --------------------------------------------------

category_returns = (
    perf.groupby("category")["return_3yr_pct"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
category_returns.plot(kind="bar")
plt.title("Average 3-Year Return by Category")
plt.ylabel("Return (%)")
plt.tight_layout()

plt.savefig(
    REPORTS / "category_returns.png"
)

plt.show()

# --------------------------------------------------
# 2. Risk Distribution
# --------------------------------------------------

plt.figure(figsize=(8,5))

sns.countplot(
    data=perf,
    x="risk_grade"
)

plt.title("Risk Grade Distribution")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig(
    REPORTS / "risk_distribution.png"
)

plt.show()

# --------------------------------------------------
# 3. Age Group Distribution
# --------------------------------------------------

plt.figure(figsize=(8,5))

sns.countplot(
    data=txn,
    x="age_group"
)

plt.title("Investor Age Group Distribution")
plt.tight_layout()

plt.savefig(
    REPORTS / "age_distribution.png"
)

plt.show()

# --------------------------------------------------
# 4. Gender Distribution
# --------------------------------------------------

plt.figure(figsize=(6,6))

txn["gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Gender Distribution")

plt.savefig(
    REPORTS / "gender_distribution.png"
)

plt.show()

print("All charts created successfully!")
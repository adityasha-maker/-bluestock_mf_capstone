import sqlite3

conn = sqlite3.connect(
    r"C:\Users\sharm\OneDrive\Desktop\bluestock_mf.db"
)

cursor = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(table, ":", count)

conn.close()
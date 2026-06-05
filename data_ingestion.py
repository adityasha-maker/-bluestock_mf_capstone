from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw")

def audit_dataset(file_path):
    print("=" * 80)
    print(f"FILE: {file_path.name}")

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    return df

def main():
    csv_files = list(RAW_PATH.glob("*.csv"))
    for file in csv_files:
        audit_dataset(file)

if __name__ == "__main__":
    main()

from pathlib import Path
import pandas as pd

RAW_PATH = Path(r"C:\Users\sharm\OneDrive\Desktop\DATASETS CSV")

for file in RAW_PATH.glob('*.csv'):
    df = pd.read_csv(file)
    print('='*80)
    print(file.name)
    print(df.shape)
    print(df.dtypes)
    print(df.head())

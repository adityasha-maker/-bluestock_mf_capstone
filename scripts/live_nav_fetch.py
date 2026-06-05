import requests
import pandas as pd
from pathlib import Path

RAW_PATH = Path('data/raw')
schemes = {'hdfc_top100':125497,'sbi_bluechip':119551,'icici_bluechip':120503,'nippon_largecap':118632,'axis_bluechip':119092,'kotak_bluechip':120841}

for name, code in schemes.items():
    url=f'https://api.mfapi.in/mf/{code}'
    print(url)

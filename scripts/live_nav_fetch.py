import requests
import pandas as pd
from pathlib import Path

output_dir = Path("data/raw")

schemes = {
    "HDFC": 125497,
    "SBI": 119551,
    "ICICI": 120503,
    "NIPPON": 118632,
    "AXIS": 119092,
    "KOTAK": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = output_dir / f"{fund_name}_live_nav.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Downloaded: {fund_name}")

    else:
        print(f"Failed: {fund_name}")
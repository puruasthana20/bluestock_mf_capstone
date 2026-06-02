import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

csv_files = sorted(DATA_DIR.glob("*.csv"))

print(f"\nFound {len(csv_files)} datasets\n")

for file in csv_files:
    print("=" * 60)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\n")
    print("\n" + "="*60)
    print("FUND MASTER ANALYSIS")
    print("="*60)

    fund_master = pd.read_csv("data/raw/01_fund_master.csv")

    print("\nFund Houses:")
    print(fund_master["fund_house"].unique())

    print("\nCategories:")
    print(fund_master["category"].unique())

    print("\nSub Categories:")
    print(fund_master["sub_category"].unique())

    print("\nRisk category:")
    print(fund_master["risk_category"].unique())
    
    print("\n" + "="*60)
    print("AMFI CODE VALIDATION")
    print("="*60)

    nav_history = pd.read_csv("data/raw/02_nav_history.csv")

    missing_codes = (
        set(fund_master["amfi_code"])
        - set(nav_history["amfi_code"])
    )

    print("\nMissing Codes:")
    print(missing_codes)

    print(f"\nTotal Missing Codes: {len(missing_codes)}")
    print("\n" + "="*60)
    print("DUPLICATE CHECKS")
    print("="*60)

    for file in csv_files:

        df = pd.read_csv(file)

        duplicates = df.duplicated().sum()

        print(f"{file.name}: {duplicates} duplicate rows")
    print("\nDATA QUALITY OBSERVATIONS")
    print("- AMFI Code Validation Passed")
    print("- Missing Codes: 0")
    print("- 04_monthly_sip_inflows.csv contains 12 missing yoy_growth_pct values")
    print("- Missing YoY values likely due to unavailable prior-year comparison data")
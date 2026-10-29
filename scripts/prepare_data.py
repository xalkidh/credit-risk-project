"""Download the UCI Default of Credit Card Clients dataset and clean it.

Output: data/credit_default_clean.csv
"""
from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo

OUTPUT_PATH = Path("data/credit_default_clean.csv")

# Descriptive names for X1-X23 and the target Y (from the UCI documentation)
COLUMN_NAMES = (
    ["LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE"]
    + [f"PAY_{i}" for i in range(1, 7)]
    + [f"BILL_AMT{i}" for i in range(1, 7)]
    + [f"PAY_AMT{i}" for i in range(1, 7)]
    + ["DEFAULT"]
)


def main():
    # Download the dataset (UCI id 350) and join features with the target
    dataset = fetch_ucirepo(id=350)
    df = dataset.data.features.join(dataset.data.targets)
    df.columns = COLUMN_NAMES

    # Merge undocumented category codes into the "other" category
    df["EDUCATION"] = df["EDUCATION"].replace({0: 4, 5: 4, 6: 4})
    df["MARRIAGE"] = df["MARRIAGE"].replace({0: 3})

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {OUTPUT_PATH} with shape {df.shape}")


if __name__ == "__main__":
    main()
import pandas as pd
from pandas import DataFrame


def save_unique_data():
    df: DataFrame = pd.read_csv("task1.csv")
    df.drop_duplicates(inplace=True)
    df.to_csv("task1_without_dupl.csv", index=False)


if __name__ == "__main__":
    save_unique_data()

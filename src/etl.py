import pandas as pd

def extract():
    df = pd.read_csv("../data/sales_data_sample.csv")
    return df

def transform(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values("date")
    return df

def load():
    df = extract()
    df = transform(df)
    print(df.head())

if __name__ == "__main__":
    load()
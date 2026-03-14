"""
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

#df = pd.read_csv("../data/sales_data_sample.csv")
df = pd.read_csv("../data/sales_data_sample.csv", encoding="latin1")
print(df.columns)

#df['date'] = pd.to_datetime(df['date'])
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

df = df.rename(columns={
    "ORDERDATE": "ds",
    "SALES": "y"
})

df = df[['ds','y']]

model = Prophet()

model.fit(df)

#future = model.make_future_dataframe(periods=7)
future = model.make_future_dataframe(periods=30)

forecast = model.predict(future)

model.plot(forecast)

plt.title("Retail Demand Forecast")

plt.show()
"""

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

#df = pd.read_csv("../data/sales_data_sample.csv")
df = pd.read_csv("../data/sales_data_sample.csv", encoding="latin1")
print(df.columns)

#df['date'] = pd.to_datetime(df['date'])
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])


df = df.groupby("ORDERDATE")["SALES"].sum().reset_index()

df = df.rename(columns={
    "ORDERDATE": "ds",
    "SALES": "y"
})
#df = df.rename(columns={
#    "ORDERDATE": "ds",
#    "SALES": "y"
#})

#df = df[['ds','y']]

model = Prophet()

model.fit(df)

#future = model.make_future_dataframe(periods=7)
future = model.make_future_dataframe(periods=30)

forecast = model.predict(future)

model.plot(forecast)

plt.title("Retail Demand Forecast")

plt.show()
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/sales_data_sample.csv", encoding="latin1")

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Title
st.title("Retail Demand Forecasting Dashboard")

# Show dataset
st.subheader("Sales Dataset")
st.write(df.head())

# Sales trend
st.subheader("Sales Trend Over Time")

daily_sales = df.groupby("ORDERDATE")["SALES"].sum().reset_index()

fig, ax = plt.subplots()

ax.plot(daily_sales["ORDERDATE"], daily_sales["SALES"])

ax.set_xlabel("Date")
ax.set_ylabel("Sales")

st.pyplot(fig)

# Country filter
st.subheader("Country Sales Analysis")

country = st.selectbox("Select Country", df["COUNTRY"].unique())

filtered = df[df["COUNTRY"] == country]

st.write(filtered.head())
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/sales_data_sample.csv", encoding="latin1")

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Title
st.title("Retail Demand Forecasting Dashboard")

# Show dataset
st.subheader("Sales Dataset")
st.write(df.head())

# Sales trend
st.subheader("Sales Trend Over Time")

daily_sales = df.groupby("ORDERDATE")["SALES"].sum().reset_index()

fig, ax = plt.subplots()

ax.plot(daily_sales["ORDERDATE"], daily_sales["SALES"])

ax.set_xlabel("Date")
ax.set_ylabel("Sales")

st.pyplot(fig)

# Country filter
st.subheader("Country Sales Analysis")

#country = st.selectbox("Select Country", df["COUNTRY"].unique())
country = st.selectbox("Select Country", df["COUNTRY"].unique())
filtered = df[df["COUNTRY"] == country]
st.write(filtered.head())



filtered = df[df["COUNTRY"] == country]

top_products = df.groupby("PRODUCTLINE")["SALES"].sum()

st.bar_chart(top_products)

st.write(filtered.head())
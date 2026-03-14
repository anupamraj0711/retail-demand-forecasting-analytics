"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/sales_data.csv")

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
import os

# Get project root folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Path to dataset
data_path = os.path.join(BASE_DIR, "data", "sales_data_sample.csv")

# Load dataset
df = pd.read_csv(data_path, encoding="latin1")

# Convert date column
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

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

# Product sales
st.subheader("Top Product Lines")

top_products = df.groupby("PRODUCTLINE")["SALES"].sum()

st.bar_chart(top_products)

filtered = df[df["COUNTRY"] == country]
st.write(filtered.head())
# Retail Demand Forecasting Analytics System

## Overview

This project analyzes historical retail sales data and predicts future product demand using time-series forecasting. The system processes retail datasets, stores the processed data in MongoDB, and provides an interactive dashboard for sales analytics and visualization.

The goal of this project is to demonstrate a complete data analytics pipeline including data processing, database storage, demand forecasting, and dashboard visualization.

---

## Dashboard Preview

![Dashboard](images/dashboard.png)

The Streamlit dashboard allows users to explore sales trends and analyze retail data interactively.

---

## Features

* Data preprocessing and cleaning using **Python and Pandas**
* Retail sales trend analysis
* Demand forecasting using **Facebook Prophet**
* Storage of processed data in **MongoDB**
* Interactive analytics dashboard using **Streamlit**
* Visualization of sales trends over time
* Country-based filtering and exploration

---

## Project Architecture

```
Retail Dataset
      ↓
Data Cleaning & Transformation (Pandas)
      ↓
Database Storage (MongoDB)
      ↓
Demand Forecasting (Prophet)
      ↓
Interactive Dashboard (Streamlit)
```

---

## Project Structure

```
retail-demand-forecasting
│
├── data
│   └── sales_data.csv
│
├── src
│   ├── etl.py
│   ├── forecast.py
│   └── store_mongodb.py
│
├── dashboard
│   └── app.py
│
├── images
│   └── dashboard.png
│
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* Pandas
* Facebook Prophet
* MongoDB
* Streamlit
* Matplotlib

---

## Dataset

The dataset contains historical retail sales records including:

* Order number
* Product details
* Quantity ordered
* Sales amount
* Order date
* Customer information
* Country and territory

This data is used to analyze sales trends and forecast future demand.

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/retail-demand-forecasting.git
```

Navigate into the project directory:

```
cd retail-demand-forecasting
```

Install required dependencies:

```
pip install -r requirements.txt
```

---

## Running the Forecasting Script

```
python src/forecast.py
```

This script trains a forecasting model and predicts future sales demand using the Prophet time-series model.

---

## Running the Streamlit Dashboard

```
streamlit run dashboard/app.py
```

After running the command, open the following URL in your browser:

```
http://localhost:8501
```

The dashboard will display sales trends and allow exploration of the dataset.

---

## Future Improvements

* Integration with real-time retail datasets
* Advanced forecasting models
* Product-level demand prediction
* Inventory risk detection
* Deployment of the dashboard to cloud platforms

---

## Author

**Anupam Raj**

B.Tech CSE,NIIT University
Interested in Data Analytics, AI Systems, and Applied Machine Learning.

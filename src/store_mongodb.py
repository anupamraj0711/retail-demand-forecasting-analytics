import pandas as pd
from pymongo import MongoClient

# Load dataset
#df = pd.read_csv("../data/sales_data_sample.csv")
df = pd.read_csv("../data/sales_data_sample.csv", encoding="latin1")


# Convert date
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Connect MongoDB
client = MongoClient("mongodb+srv://anupam4:anupam@cluster0.4evyxt8.mongodb.net/?appName=Cluster0")

db = client["retail_database"]

collection = db["sales_data"]

# Convert dataframe to dictionary
data = df.to_dict("records")

# Insert into MongoDB
collection.insert_many(data)

print("Data stored successfully in MongoDB")
import pandas as pd
from pymongo import MongoClient

#df = pd.read_csv("../data/sales_data_sample.csv")
df = pd.read_csv("../data/sales_data_sample.csv", encoding="latin1")

client = MongoClient("mongodb+srv://anupam4:anupam@cluster0.4evyxt8.mongodb.net/?appName=Cluster0")

db = client["retail_db"]

collection = db["sales"]

data = df.to_dict("records")

collection.insert_many(data)

print("Data stored in MongoDB")
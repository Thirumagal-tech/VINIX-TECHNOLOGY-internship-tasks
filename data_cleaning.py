import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\Admin\Downloads\daily.csv")
print("Original Dataset:")
print(data)
print("\nMissing Values:")
print(data.isnull().sum())
print("\nShape of Data:")
print(data.shape)
print("\nDataset Information:")
data.info()
print("\nDuplicate Records:")
print(data.duplicated().sum())
data = data.drop_duplicates()
data.columns = data.columns.str.strip()

print("\nColumn Names:")
print(data.columns)
text_columns = data.select_dtypes(include=["object"]).columns
print("\nText Columns:")
print(text_columns)
for column in text_columns:
    data[column] = data[column].astype(str).str.strip()
print("\nText Columns Cleaned Successfully!")
if "country" in data.columns:
    data["country"] = data["country"].fillna("Unknown")
if "countries" in data.columns:
    data["countries"] = data["countries"].fillna("Unknown")
if "also_in" in data.columns:
    data["also_in"] = data["also_in"].fillna("Not Available")
data["date"] = pd.to_datetime(data["date"], errors="coerce")
print("\nMissing Values After Cleaning:")
print(data.isnull().sum())
print("\nCleaned Dataset:")
print(data.head())

print("\nShape After Cleaning:")
print(data.shape)

print("\nDataset Cleaned Successfully!")
# DATA TRANSFORMATION
data["followers_millions"] = data["followers"] / 1000000
print("\nFollowers in Millions:")
print(data["followers_millions"])
data["year"] = data["date"].dt.year
data["month"] = data["date"].dt.month
data["day"] = data["date"].dt.day
print("\nYear, Month, Day:")
print(data[["year", "month", "day"]].head())
data["follower_category"] = pd.cut(
    data["followers"],
    bins=[0, 100000, 200000, 500000, 1000000, float("inf")],
    labels=["low", "medium", "high", "very high", "extreme"]
)
print("\nFollower Category:")
print(data["follower_category"])
if "category" in data.columns:
    data["category_code"] = data["category"].astype("category").cat.codes

    print("\nCategory Codes:")
    print(data["category_code"])
print("\nTransformed Dataset:")
print(data.head())
print("\nFinal Dataset Information:")
data.info()
data.to_csv(r"C:\Users\Admin\Downloads\cleaned_daily.csv", index=False)
data.to_csv(r"C:\Users\Admin\Downloads\transformed_daily.csv", index=False)
print("\nDataset Transformed Successfully!")
print("Files Saved:")
print("1. cleaned_daily.csv")
print("2. transformed_daily.csv")


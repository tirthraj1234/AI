import pandas as pd

df = pd.read_csv("Day_2/dataset/employee_missing.csv")# to get file

print(df)

print(df.isnull())# to check missing values

print(df.isnull().sum())# count missing values

clean_df = df.dropna()# remove missing values

print(clean_df)

df["Age"] = df["Age"].fillna(df["Age"].mean())# fill empty place with mean

df["Salary"] = df["Salary"].fillna(df["Salary"].median())# fill with median

df["Department"] = df["Department"].fillna(df["Department"].mode()[0])# fill with mode

print(df)


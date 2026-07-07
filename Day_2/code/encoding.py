import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Day_2/dataset/employee_encoding.csv")# to get data

print(df)


# label encoding
label_encoder = LabelEncoder()

df["Gender"] = label_encoder.fit_transform(df["Gender"])

print(df)

# one-hot encoding
df = pd.get_dummies(df, columns=["Department"])

print(df)


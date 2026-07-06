import pandas as pd

df = pd.read_csv("Day_1/dataset/employees.csv")

print(df)

print(df.head())# print first 5 rows

print(df.tail())# print last 5 rows

print(df.info())# dataset information

print(df.describe())# statistical information

print(df.columns)# display columns name 

print(df["Salary"])# select one column

print(df[["Name", "Salary"]])# select multiple column

# filter data
high_salary = df[df["Salary"] > 40000]

print(high_salary)

# add new column
df["Bonus"] = df["Salary"] * 0.10

print(df)

# drop a column
new_df = df.drop(columns=["Bonus"])

print(new_df)

# creates a new file
# df.to_csv("Day_1/dataset/employees_updated.csv", index=False)
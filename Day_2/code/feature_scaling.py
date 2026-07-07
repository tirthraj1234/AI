import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("Day_2/dataset/employee_scaling.csv")# read dataset

print(df)

# standardization
scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print("Standardized Data:")
print(scaled_df)

# normalization
min_max = MinMaxScaler()

normalized_data = min_max.fit_transform(df)

normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print("Normalized Data:")
print(normalized_df)






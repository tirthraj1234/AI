import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [25, 30, 35],
    "Salary": [30000, 50000, 80000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

print(scaled_data)
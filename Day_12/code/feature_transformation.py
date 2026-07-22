import numpy as np
import pandas as pd
from sklearn.preprocessing import PowerTransformer

# Sample Data
data = {
    "Income": [1000, 1500, 2500, 5000, 10000]
}

df = pd.DataFrame(data)

# Log Transformation
df["Log_Income"] = np.log1p(df["Income"])

# Square Root Transformation
df["Sqrt_Income"] = np.sqrt(df["Income"])

# Power Transformation (Yeo-Johnson)
pt = PowerTransformer(method="yeo-johnson")
df["Power_Income"] = pt.fit_transform(df[["Income"]])

print(df)
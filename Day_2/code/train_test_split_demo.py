import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("Day_2/dataset/customer_data.csv")

print(df)

# separate feature and target
X = df[["Age", "Salary"]]
y = df["Purchased"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# display result
print("Training Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Labels:")
print(y_train)

print("\nTesting Labels:")
print(y_test)
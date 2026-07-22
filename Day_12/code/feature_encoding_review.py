import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

# ---------------------------------------
# Sample Dataset
# ---------------------------------------

data = {
    "Color": ["Red", "Blue", "Green", "Red", "Blue"],
    "Size": ["Small", "Medium", "Large", "Medium", "Small"],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "Purchased": [1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print("=" * 60)
print("Original Dataset")
print("=" * 60)
print(df)

# =====================================================
# 1. Label Encoding
# =====================================================

print("\n" + "=" * 60)
print("1. Label Encoding")
print("=" * 60)

label_df = df.copy()

label_encoder = LabelEncoder()
label_df["Color"] = label_encoder.fit_transform(label_df["Color"])

print(label_df)

# =====================================================
# 2. One-Hot Encoding
# =====================================================

print("\n" + "=" * 60)
print("2. One-Hot Encoding")
print("=" * 60)

onehot_df = pd.get_dummies(df, columns=["Color"])

print(onehot_df)

# =====================================================
# 3. Ordinal Encoding
# =====================================================

print("\n" + "=" * 60)
print("3. Ordinal Encoding")
print("=" * 60)

ordinal_df = df.copy()

encoder = OrdinalEncoder(
    categories=[["Small", "Medium", "Large"]]
)

ordinal_df["Size"] = encoder.fit_transform(ordinal_df[["Size"]])

print(ordinal_df)

# =====================================================
# 4. Frequency Encoding
# =====================================================

print("\n" + "=" * 60)
print("4. Frequency Encoding")
print("=" * 60)

frequency_df = df.copy()

frequency = frequency_df["City"].value_counts()

frequency_df["City"] = frequency_df["City"].map(frequency)

print(frequency_df)

# =====================================================
# 5. Target Encoding (Simple Example)
# =====================================================

print("\n" + "=" * 60)
print("5. Target Encoding")
print("=" * 60)

target_df = df.copy()

target_mean = target_df.groupby("City")["Purchased"].mean()

target_df["City"] = target_df["City"].map(target_mean)

print(target_df)

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("Encoding Review Completed Successfully!")
print("=" * 60)
print("""
Techniques Demonstrated:
1. Label Encoding
2. One-Hot Encoding
3. Ordinal Encoding
4. Frequency Encoding
5. Target Encoding
""")
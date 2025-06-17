import pandas as pd

# Load the dataset
file_path = "data/raw/MachineLearningRating_v3.txt"
df = pd.read_csv(file_path, sep="|")

# Prepare metrics
df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
df["HasClaim"] = df["TotalClaims"] > 0

# Drop rows with missing key fields
df_clean = df.dropna(subset=["Province", "Gender", "PostalCode", "TotalClaims", "TotalPremium"])

# Display basic structure for hypothesis testing
print("✅ Data Ready for Task 3")
print(f"Rows: {df_clean.shape[0]}")
print(f"Provinces: {df_clean['Province'].nunique()}")
print(f"PostalCodes: {df_clean['PostalCode'].nunique()}")
print(f"Genders: {df_clean['Gender'].unique().tolist()}")

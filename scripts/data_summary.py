import pandas as pd

# File path
DATA_PATH = r"D:\@kaim\insurance-analytics-kaim-week3\data\raw\MachineLearningRating_v3.txt"

# Load data
df = pd.read_csv(DATA_PATH, sep='|', low_memory=False)

# --- Summary ---
print("\n🔍 Dataset Shape:", df.shape)

# Column types
print("\n📊 Column Data Types:")
print(df.dtypes.value_counts())
print(df.dtypes)

# Numeric vs Categorical
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'bool']).columns.tolist()

print("\n🧮 Numeric Columns:", numeric_cols)
print("\n🔡 Categorical Columns:", categorical_cols)

# Descriptive Stats
print("\n📈 Summary Statistics (Numerical):")
print(df[numeric_cols].describe().T)

# Missing values
print("\n❓ Missing Values Summary:")
missing = df.isnull().sum()
missing = missing[missing > 0]
print(missing.sort_values(ascending=False))

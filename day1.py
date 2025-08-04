# Step 1: Upload CSV file
from google.colab import files
uploaded = files.upload()

# Step 2: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Step 3: Read the uploaded CSV
file_name = next(iter(uploaded))
df = pd.read_csv(file_name)

# Step 4: Show basic info
print("Initial Data Preview:")
print(df.head())
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# Step 5: Handle missing values (example: age, gender)
if 'age' in df.columns:
    df['age'] = df['age'].fillna(df['age'].median())
if 'gender' in df.columns:
    df['gender'] = df['gender'].fillna(df['gender'].mode()[0])

# Step 6: One-hot encode categorical features (example: gender, city)
for col in df.select_dtypes(include='object').columns:
    df = pd.get_dummies(df, columns=[col], drop_first=True)

# Step 7: Standardize numeric columns (example: age, income)
num_cols = df.select_dtypes(include='number').columns
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Step 8: Visualize and remove outliers (using income as example)
if 'income' in df.columns:
    sns.boxplot(x=df['income'])
    plt.title("Boxplot of Income")
    plt.show()

    Q1 = df['income'].quantile(0.25)
    Q3 = df['income'].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df['income'] >= lower) & (df['income'] <= upper)]

# Step 9: Final output
print("\nCleaned Data Preview:")
print(df.head())
print("\nData shape after cleaning:", df.shape)
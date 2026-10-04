import pandas as pd

# VEDA TECHNOLOGY - Day 18
# Task: Select Dataset Columns using Pandas loc and iloc

df = pd.read_csv("iris_sample.csv")

print("Original Dataset:")
print(df)

# Using loc - label based selection
print("\n1. Single column using loc:")
print(df.loc[:, "species"])

print("\n2. Multiple columns using loc:")
print(df.loc[:, ["sepal_length", "petal_length", "species"]])

print("\n3. Specific rows and columns using loc:")
print(df.loc[0:3, ["id", "sepal_length", "species"]])

# Using iloc - integer position based selection
print("\n4. First 3 rows and first 3 columns using iloc:")
print(df.iloc[0:3, 0:3])

print("\n5. Rows 2 to 5 and columns 1 to 4 using iloc:")
print(df.iloc[2:6, 1:5])

print("\n6. Single value using iloc:")
print(df.iloc[0, 5])

print("\nTask completed successfully.")

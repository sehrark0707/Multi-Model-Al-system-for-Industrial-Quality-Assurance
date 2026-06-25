import pandas as pd
import numpy as np

print("--- Pandas Series ---")
scores = pd.Series([76, 94, 82, 89, 91], name="Scores")
print(scores)
print("Mean scores:", scores.mean())

print("\n--- Creating a DataFrame ---")
data = {
    "Name": ["Leo", "Maya", "Omar", "Chloe", "Zion"],
    "Age": [19, 20, 19, 22, 21],
    "Scores": [76, 94, 82, 89, 91],
    "City": ["Tokyo", "Berlin", "Tokyo", "London", "Berlin"]
}
df = pd.DataFrame(data)
print(df)

print("\n--- Indexing & Selecting Data ---")
print(df.loc[0:2])
print(df.iloc[0:2, 0:2])
print(df["Name"])

print("\n--- Filtering Data ---")
high_scorers = df[df["Scores"] > 85]
print(high_scorers)
tokyo_students = df[df["City"] == "Tokyo"]
print(tokyo_students)

print("\n--- Adding/Modifying Columns ---")
df["Grade"] = df["Scores"].apply(lambda x: "A" if x >= 85 else "B")
print(df)

print("\n--- Grouping & Aggregating ---")
city_avg = df.groupby("City")["Scores"].mean()
print(city_avg)

print("\n--- Handling Missing Values ---")
df_with_nan = df.copy()
df_with_nan.loc[2, "Scores"] = np.nan
print(df_with_nan)
print(df_with_nan.isnull().sum())
df_filled = df_with_nan.copy()
df_filled["Scores"] = df_filled["Scores"].fillna(df_filled["Scores"].mean())
print(df_filled)

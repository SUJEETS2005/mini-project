# import pandas as pd

# data = {
#     "Name": ["Arun", "Bala", "Charan"],
#     "Math": [85, 90, 78],
#     "Science": [88, 92, 80]
# }

# df = pd.DataFrame(data)

# print(df)c
# import pandas as pd

# df = pd.read_csv("Students.csv")

# print("--- Columns ---")
# print(df.columns)

# df['total_score'] = df['math score'] + df['reading score'] + df['writing score']
# df['average_score'] = df['total_score'] / 3

# print("\n--- Top 5 Records ---")
# print(df.head())

# brilliant = df[df['average_score'] > 90]
# print("\n--- High Scorers ---")
# print(brilliant)

# print("\n--- Average Score by Gender ---")
# print(df.groupby('gender')['total_score'].mean())

# print("\n--- Parental Education Counts ---")
# print(df['parental level of education'].value_counts())

# top_10 = df.sort_values(by='total_score', ascending=False).head(10)
# print("\n--- Top 10 Students ---")
# print(top_10)

import pandas as pd
import numpy as np

ds = pd.read_csv("students.csv")
#print(ds)

#print(ds.head())

#print(ds.isnull())

# ds["math score"] = ds["math score"].fillna(ds["math score"].mean())
# ds["reading score"] = ds["reading score"].fillna(ds["reading score"].mean())
# ds["writing score"] = ds["writing score"].fillna(ds["writing score"].mean())

# print(ds)
# ds = ds.drop_duplicates()
# print(ds)
ds = ds.rename(columns={"math score": "Math_Score"})
filtered = ds[ds["Math_Score"] > 80]

print(filtered)
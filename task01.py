import pandas as pd
import numpy as np

dataset = pd.read_csv("students.csv")

print("Missing values:\n", dataset.isnull().sum())

dataset = dataset.drop_duplicates()

dataset = dataset.fillna(0)

data_array = dataset[["math score","reading score","writing score"]].to_numpy()
print("\nNumPy Mean:", np.mean(data_array))

group_data = dataset.groupby("gender")[["math score","reading score","writing score"]].mean()
print("\nGroupBy Mean:\n", group_data)

agg = dataset.groupby("gender").agg({
    "math score":"mean",
    "reading score":"max",
    "writing score":"min"
})
print("\nAggregation:\n", agg)

scholarship = {
    "gender":["female","male"],
    "scholarship":[5000,4000]
}

scholarship_df = pd.DataFrame(scholarship)

merged = pd.merge(dataset, scholarship_df, on="gender")
print("\nMerged Data:\n", merged.head())

corr = dataset[["math score","reading score","writing score"]].corr()
print("\nCorrelation:\n", corr)
import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.columns)

group_col = "gender"
num_col = "math score"

grouped = df.groupby(group_col)[num_col]

avg_value = grouped.mean()
sum_value = grouped.sum()
count_value = grouped.count()

print("Average:\n", avg_value)
print("Sum:\n", sum_value)
print("Count:\n", count_value)


multi_agg = df.groupby(group_col)[num_col].agg(["mean","sum","count"])
print("Multiple Aggregations:\n", multi_agg)


extra_data = pd.DataFrame({
    "gender": df["gender"],
    "Bonus": [1000]*len(df)
})

merged_df = pd.merge(df, extra_data, on="gender", how="left")
print("Merged Data:\n", merged_df.head())


df["Total_score"] = df["math score"] + df["reading score"] + df["writing score"]
print(df[["gender","Total_score"]].head())


corr = df[["math score","reading score","writing score"]].corr()
print("Correlation Matrix:\n", corr)
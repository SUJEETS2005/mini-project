# import pandas as pd

# data = {
#     "Name": ["Arun", "Bala", "Charan"],
#     "Math": [85, 90, 78],
#     "Science": [88, 92, 80]
# }

# df = pd.DataFrame(data)

# print(df)
import pandas as pd

df = pd.read_csv("Students.csv")

print("--- Columns ---")
print(df.columns)

df['total_score'] = df['math score'] + df['reading score'] + df['writing score']
df['average_score'] = df['total_score'] / 3

print("\n--- Top 5 Records ---")
print(df.head())

brilliant = df[df['average_score'] > 90]
print("\n--- High Scorers ---")
print(brilliant)

print("\n--- Average Score by Gender ---")
print(df.groupby('gender')['total_score'].mean())

print("\n--- Parental Education Counts ---")
print(df['parental level of education'].value_counts())

top_10 = df.sort_values(by='total_score', ascending=False).head(10)
print("\n--- Top 10 Students ---")
print(top_10)
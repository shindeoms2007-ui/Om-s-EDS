import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# write your code here..

print("First five rows:")
print(data.head())

# Average age
print("Average age:", round(data['Age'].mean(), 2))

# Students with grade up to B (i.e., A or B)
filtered = data[data['Grade'].isin(['A', 'B'])]

print("Students with a grade up to B")
print(filtered)
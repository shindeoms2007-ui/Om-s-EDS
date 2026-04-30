import pandas as pd

# Take inputs from the user to create a list of numbers
numbers = list(map(int, input().split()))
df=pd.Series(numbers)
# Create a Pandas series from the list of numbers

# Grouping by even and odd numbers and calculating the mean
grouped = df.groupby(df % 2== 0).mean()

# Display the mean of even and odd numbers with labels
grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]
print("Mean of even and odd numbers:")
print(grouped)

import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

pair_counter = Counter()

grouped = df.groupby('Date')['Product'].apply(list)

for products in grouped:
    unique_products = list(set(products))
    pairs = combinations(sorted(unique_products), 2)
    pair_counter.update(pairs)

max_count = max(pair_counter.values())

for pair, count in pair_counter.items():
    if count == max_count:
        print(f"{pair[0]} and {pair[1]}: {count} times")








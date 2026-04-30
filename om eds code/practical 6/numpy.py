import numpy as np

A = np.array([
    [120, 122, 125],   
    [130, 128, 135],   
    [110, 115, 118]    
])

B = np.array([
    [130, 135, 140],   
    [140, 138, 150],   
    [115, 120, 130]    
])

print("morning readings (A):\n", A)
print("evening readings (B):\n", B)


daily_avg = (A + B) / 2
column_avg = np.mean(daily_avg, axis=0)

print("\ndaily average BP (column-wise):", column_avg)


difference = B - A
print("\ndifference (evening - morning):\n", difference)


increase_mask = difference > 10
print("\nreadings where BP increased > 10:\n", increase_mask)


print("\nvalues where increase > 10:\n", difference[increase_mask])


multiplication = A * B
print("\nelement-wise multiplication:\n", multiplication)


max_bp = np.max([A, B])
print("\nmaximum BP recorded:", max_bp)
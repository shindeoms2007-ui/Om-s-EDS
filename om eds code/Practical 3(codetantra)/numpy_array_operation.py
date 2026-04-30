import numpy as np
row,colm = map(int,input().split())
if row==0 and colm==0:
	matrix = np.empty((row,colm), dtype = int)
else:
	matrix = np.array([input().split()for i in range(row)],dtype=int)
print(matrix)
print(np.ndim(matrix))
print(np.shape(matrix))
print(np.size(matrix))
# write your code here...

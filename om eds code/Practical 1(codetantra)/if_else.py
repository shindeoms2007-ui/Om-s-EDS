import math
n=int(input())
if n>=1 and n<=9:
	print(n**2)
elif 10<=n<100:
	print(f"{math.sqrt(n):.2f}")
elif 100<=n<=999:
	print(f"{math.cbrt(n):.2f}")
else:
	print("Invalid")
arr = list(map(int,input().split()))
key = int(input("Enter the key: "))
index = -1
for i in range(len(arr)):
    if arr[i] == key:
        index = i
        break   
if index == -1:
    print("Key not found")
else:
    print("Key found at index:", index)
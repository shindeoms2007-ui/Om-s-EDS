n = int(input("Enter the number: "))   #taking input from user
i=0
for i in range(i,n):                    #use of nested for loops
    for j in range(0,i+1):
        print(j+1, end=" ")          #printing numbers pattern
    print( ) 
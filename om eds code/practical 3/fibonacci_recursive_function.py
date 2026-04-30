def fibonnaci(n): #function defining
    if(n<=0):  
        return "invalid input"
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)      #calculating fibonacci number  
n= int(input("Enter the position of Fibonacci number: "))   #taking input from the user
print(fibonnaci(n)) #calling the function
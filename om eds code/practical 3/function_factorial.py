def factorial(n):    #function defining
    if n==0 or n==1:   #conditions for calculating factorial
        return 1
    elif n<0:
        return"invalid input"
    else:                         
        return n*factorial(n-1)   #calculating factorial
n= int(input("Enter the number: "))     #taking input from the user
print(factorial(n))     #calling the function and printing the result
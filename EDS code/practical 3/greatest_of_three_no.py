def numbers(a,b,c):        #defining function
    if (a>b) and (a>c):     #conditional statement
        return a            #return value if condition is true
    elif (b>a) and (b>c):
        return b
    elif (a==b and b==c):
        return ("All numbers are equal")
    else:
        return c
a = int(input("Enter the first number: "))        #taking input from user
b = int(input("Enter the second number: "))       #taking input from user
c = int(input("Enter the third number: "))        #taking input from user
print(numbers(a,b,c))                             #calling the function
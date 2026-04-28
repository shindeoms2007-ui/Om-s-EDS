def check_number_sign(a):
    if (a>0):                   #conditional statements
        return "Positive"       #return value if conditionn is true
    elif (a<0):
        return "Negative"
    else:
        return "Zero"   
a = int(input("Enter the number: "))       #taking input from user
print(check_number_sign(a))                #calling the function
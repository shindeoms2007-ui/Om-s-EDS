pno = lambda x: "positive" if x>0 else "negative" if x<0 else "zero"       #lambda function for checking if number is positive, negative or zero
n = float(input("Enter the number:"))   #taking input from user
print(pno(n))   #printing return of lambda function 
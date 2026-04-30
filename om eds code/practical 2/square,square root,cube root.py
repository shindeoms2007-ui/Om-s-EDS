import math #importing math module to use mathematical functions
a = float(input("Enter a number: ")) #taking input from user
if(0<a<10): #  checking number for sqaring the number
    print("Square of the number is: ", a**2)
elif(10<=a<100): #checking number for finding the square root of the number
    print("Square root of the number is: ", math.sqrt(a))
else: #checking number for finding the cube root of the number
    print("Cube root of the number is: ", math.cbrt(a))        
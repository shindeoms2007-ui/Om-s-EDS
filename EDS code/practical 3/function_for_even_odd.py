def evenodd(a):        #defining function
 if (a%2==0):             #conditional satatement
    return("even")        #return value if condition is true
 else:
    return("odd")
a = int(input("Enter the number"))      #taking input from user
print(evenodd(a))            #calling the function
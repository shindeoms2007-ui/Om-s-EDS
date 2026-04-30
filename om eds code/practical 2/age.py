#taking input from user
a = int(input("Enter your age: "))
#checking the age group using conditional statements
if(0<a<=5):
    print("You are a Toddler.")
elif(5<a<=12):    #other conditonal statements 
    print("You are a Child.")
elif(12<a<=19):
    print("You are a Teenager.")
elif(19<a<=65):
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")    
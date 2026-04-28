from datetime import datetime   #importing datetime module
n=int(input("Enter the birt year: "))    #taking birth year input from user
current_year=datetime.now().year    #taking current year using datetime module
age=current_year-n        # calculating age by subtracting birth year from current year  
print(f"Your age is: {age}")     #printing age to user
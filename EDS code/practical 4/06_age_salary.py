from datetime import datetime         #importing datetime module
birthdate = int(input("Enter your birthdate: ").split('-')[-1])      #using split fir taking only year
def age(birthdate):        #defining function for age calculation
    current_year = datetime.now().year         #taking current year using datetime module
    return current_year - birthdate         #calculating age by subtracting birth year from current year
def sal(salary):              #defining function for salary conversion

    dollar=0.012          #conversion rate from Indian Rupees to US Dollars
    return dollar*ind_rup                   #converting salary from Indian Rupees to US Dollars
ind_rup = float(input("Enter your salary in Indian Rupees: "))            #taking salary input from user 
print(f"Your age is: {age(birthdate)}")                    #calling and printing return of age function 
print(f"Your salary in USD is: {sal(ind_rup)}")                 #calling and printing return of salary conversion function

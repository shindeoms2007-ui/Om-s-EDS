def cal(total_course,marks):  #total_course=int(input("Enter your total courses: "))
    if any (mark<40 for mark in marks): #condition for calculating agreegated percentage
        return "fail"
    agreegated_percentage = (sum(marks)/(total_course*100))*100 #calculating agreegated percentage
    print(f"Agreegated Percentage: {agreegated_percentage:.2f}") #printing agreegated percenage
    if (agreegated_percentage>=75): #condition for grading
        return 'distinction'
    elif(agreegated_percentage>=60):
        return 'first class'
    elif(agreegated_percentage>=50):
        return 'second class'
    elif(agreegated_percentage>=40):
        return "third class"
n=int(input("Enter your total courses: ")) #taking input from user
mark=list(map(int,input().split())) #taking marks as input from user and converting it into list of integers
print(cal(n,mark)) #calling function
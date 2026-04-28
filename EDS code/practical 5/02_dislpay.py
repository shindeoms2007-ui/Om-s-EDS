number=[]
while True:
    print("1.Add")
    print("2.remove")
    print("3.display")
    print("4.Quit")
    n=int(input("Enter your choice: "))
    if n==1:
        num=int(input("Enter the number: "))
        number.append(num)
        print("List after adding the number: ",number)
    elif n==2:
        if len(number)==0:
            print("List is empty")
        else:
            x = int(input())
            if x in number:
                number.remove(x)
                
            else:
                print("Number not found in the list")
    elif n==3:
        if len(number)==0:
            print("List is empty")
        else:
            print(number)
    elif n==4:
        False
    else:
        print("Invalid Choice")
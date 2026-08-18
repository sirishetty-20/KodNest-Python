def mini_calculator(num1,num2,operation):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        if num2==0:
            print("Please enter number greator then 0")
        else:
            return num1/num2
    elif operation=="//":
        if num2==0:
            print("Please enter number greator then 0")
        else:
            return num1//num2
    else:
        print("Invalid Input")
num1=int(input("Enter the num1 value:"))
num2=int(input("Enter the num2 value:"))
operation=input("Enter the operator from these + ,- , * ,/ ,// : ")
result=mini_calculator(num1,num2,operation)
print(result)

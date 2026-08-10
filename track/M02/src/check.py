def check(number):
    if number ==0:
        return "Zero"
    elif number>0:
        return "Positive"
    else:
        return "Negative"
number=int(input("Enter the number:"))
result=check(number)
print(result)
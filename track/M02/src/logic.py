marks=int(input())
attendence=int(input())
project_completed=input()
if marks>=60 and attendence>=75:
    if project_completed=="yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
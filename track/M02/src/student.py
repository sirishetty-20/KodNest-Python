student_count=int(input("Enter the number of students:"))
total_marks=0
passed_count=0
failed_count=0
for i in range(student_count):
    mark=int(input("Enter the marks of student:"))
    total_marks=total_marks+mark
    if mark>=40:
        passed_count=passed_count+1
    else:
        failed_count=failed_count+1
print(f"Total Marks:{total_marks}")
print(f"Passed Count:{passed_count}")
print(f"Failed Count:{failed_count}")
if failed_count==0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")
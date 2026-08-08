name=input("Enter the student name:")
course=input("Enter the name of the course:")
score=input("Enter the score:")
# create a tuple
student_record=(name,course,score)
# unpack the tuple
student_name,student_course,student_score=student_record
print(f"Name:{student_record[0]}")
print(f"Course:{student_record[1]}")
print(f"Score:{student_record[2]}")


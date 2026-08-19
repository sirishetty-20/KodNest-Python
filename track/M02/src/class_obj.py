# class Student:
#     def __init__(self,roll_no,name,age,marks):
#         self.roll_no=roll_no
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def study(self):
#         print(f"{self.name} is studying")
# s1=Student(11,"Amith",22,85)
# s1.study()
# s2=Student(12,"Arun",23,90)
# s2.study()

class Student:
    def study(self,roll_no,name,age,marks):
         print(roll_no)
         print(name)
         print(age)
         print(marks)
         print(f"{name} is studying")
         print
s1=Student()
s2=Student()
s1.study(11,"Amith",22,85)
s2.study(12,"Arun",23,90)
   
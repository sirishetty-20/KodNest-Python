# class Student:
#     def __init__(self,roll_no,name,age,marks):
#         self.roll_no=roll_no
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def study(self): 
#         print(f"{self.name} is studying")

# s1=Student(11,"Amith",22,85)
# print(s1.roll_no)
# print(s1.name)
# print(s1.age)
# print(s1.marks)
# s1.study()

# s2=Student(12,"Arun",23,90)
# print(s2.roll_no)
# print(s2.name)
# print(s2.age)
# print(s2.marks)
# s2.study()
#------------------------------------------------------------------------------------------
# class Student:
#     def study(self,roll_no,name,age,marks):
#          print(roll_no)
#          print(name)
#          print(age)
#          print(marks)
#          print(f"{name} is studying")
#          
# s1=Student()
# s2=Student()
# s1.study(11,"Amith",22,85)
# s2.study(12,"Arun",23,90)

#--------------------------------------------------------------------------------------------------

class Student:
    def setter(self,roll_no,name,age,marks):
        self.__roll_no=roll_no
        self.__name=name
        self.__age=age
        self.__marks=marks

    def getter(self):
        return (f"{self.__roll_no},{self.__name},{self.__age},{self.__marks}")

    

   
    

    
    




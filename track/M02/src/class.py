class Student:
    def __init__(self,student_name,student_id,student_course,student_email,student_skills=[]):
        self.student_name=student_name
        self.student_id=student_id
        self.student_course=student_course
        self.student_email=student_email
        self.student_skills=student_skills
s1=Student("Siri",101,"Python Full Stack","sirimagadh929@gmail.com","Python")
s2=Student("Shivangi",102,"Java Full Stack","shivangi18@gmail.com","Java")
s3=Student("Dhyan",103,"Mern Stack","dhyanknshetty@gmail.com","MomgoDB")
print(s1)
print(s2)
print(s3)
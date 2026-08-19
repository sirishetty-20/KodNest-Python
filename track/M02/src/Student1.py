class StudentProfile:
    def __init__(self,id,name,course,__score):
        self.student_id=id
        self.student_name=name
        self.student_course=course
        self.__student_score=__score
    def get_score(self):
        return self.__student_score
    
    def update_score(self,new_score):
        if 0<new_score<100:
            return True
        else:
            return False
    def get_status(self):
        if  new_score


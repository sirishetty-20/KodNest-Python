class StudentProfile:
    def __init__(self,student_id,name,course,score=0.0,skills=None,is_placed=False):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.score=score
        self.skills=[] if skills is None else list(skills)
        self.is_placed=is_placed
    
    def __str__(self):
        skills_text=(",".join(self.skills) if self.skills else "N/A")
        placement_status=("Placed" if self.is_placed else "Not Placed")
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score}\n"
            f"Skills: {skills_text}\n"
            f"Placement: {placement_status}"
            )

Student=StudentProfile(101,"Kavya","DSA",98,["Python","DSA"],True)
print(Student)

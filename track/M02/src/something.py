class Course:
    def __init__(self,name,duration,trainer_name,start_date,technologies=[]):
        self.Name=name
        self.Duration=duration
        self.Trainer_name=trainer_name
        self.Start_Date=start_date
        self.Technologies=technologies
    def display(self):
        print(f"{self.Name},{self.Duration},{self.Trainer_name},{self.Start_Date},{self.Technologies}")
name=input("Enter the name:")
duration=input("Enter the duration:")
trainer_name=input("Enter the trainer name:")
start_date=input("Enter the start date:")
technologies=[]
n=int(input("Enter the number of technologies:"))
for i in range(n):
    skill=input("Enter the skill:")
    technologies.append(skill)
c1=Course(name,duration,trainer_name,start_date,technologies)
c1.display()

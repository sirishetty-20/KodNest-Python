
class Course:
    def __init__(self,name,duration,trainer_name,start_date,technologies=[]):
        self.Name=name
        self.Duration=duration
        self.Trainer_name=trainer_name
        self.Start_Date=start_date
        self.Technologies=technologies
    def display(self):
        print(f"{self.Name},{self.Duration},{self.Trainer_name},{self.Start_Date},{self.Technologies}")
    def is_tech_covered(self,tech):
        for i in self.Technologies:
            if i==tech:
                return True
        else:
            return False
    def number_of_technologies(self):
        count=0
        for i in self.Technologies:
            count=count+1
        return count
tech=input("Enter the technology to know the presence:")
c1=Course("Python","4 months","Salman Sir","15th June",["Python","SQL","EXCEL"])
c1.display()
print(c1.is_tech_covered(tech))
print(c1.number_of_technologies())

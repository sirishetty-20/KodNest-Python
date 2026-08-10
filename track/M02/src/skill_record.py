skills=[]
for i in range(5):
    skills.append(input("Enter the skills:"))
tech=tuple(skills)
print(f"Skills Record:{tech}")
print(f"First Thress: {tech[:3]}")
print(f"Last Two: {tech[-2:]}")
print(f"Alternate Skills: {tech[::2]}")
print(f"Reversed Skills: {tech[::-1]}")
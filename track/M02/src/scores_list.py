n=int(input("Enter the n value:"))
scores=[]
for i in range(n):
    num=int(input("Enter the number:"))
    scores.append(num)
search_score=int(input("Enter the value which need to be searched:"))
print(f"Highest Score:{max(scores)}")
print(f"Lowest Score:{min(scores)}")
print(f"Total Scores:{sum(scores)}")
if search_score in scores:
    print("Search score: Found")
else:
    print("Search score: Not Found")

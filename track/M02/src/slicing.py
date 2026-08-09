word=input("Enter the word:")
first=int(input("Enter the first number:"))
second=int(input("Enter the second number:"))
third=int(input("Enter the third number:"))
numbers=[first,second,third]
record=(first,second,third)
print(f"Middle:{word[1:-1]}")
print(f"First Two in list: {numbers[:2]}")
print(f"Reversed Tuple:{record[::-1]}")

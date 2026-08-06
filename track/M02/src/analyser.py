number=int(input("Enter the number:"))
total=0
positive_count=0
negative_count=0
zero_count=0
for i in range(number):
    number=int(input("Enter the number:"))
    total=total+number
    if number==0:
        zero_count=zero_count+1
    elif number>0:
        positive_count=positive_count+1
    else:
        negative_count=negative_count+1
print(f"Zero Count:{zero_count}")
print(f"Positive Count:{positive_count}")
print(f"Negative Count:{ negative_count}")
print(f"Total:{total}")

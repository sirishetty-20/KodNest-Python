# def even_num():
#     for i in range(1,101):
#         if i%2==0:
#             print(i)
# even_num()


def even_num(start,end):
    for i in range(start,end+1):
        if i%2==0:
            print(i)
start=int(input("Enter the start value:"))
end=int(input("Enter the end value: "))
even_num(start,end)
def check_prime(num):
    is_prime=True
    if num<=1:
      is_prime=False
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            print("Not a Prime number")
            break
    if is_prime==True:
        print("Prime number")
    else:
        print("Not a prime number")
num=int(input("Enter the number:"))
check_prime(num)

            







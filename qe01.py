n=int(input("enter the number:"))
factorial=1
if n<0:
    print("factorial doesn't exists")
elif n==0:
    print("factorial of o is 1")
else:
    for i in range(1,n+1):
        factorial = factorial*i
print(f"The factorial of {n} is {factorial}.")
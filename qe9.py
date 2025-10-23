s=input("enter a string:")
if len(s)>1:
    swapped=s[-1]+s[1:-1]+s[0]
else:
    swapped=s
print("swapped string:",swapped)
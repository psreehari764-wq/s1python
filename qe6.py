text=input("enter the integers:")
x=text.split(",")
x_list=[]
for item in x:
    x_list.append(item)
count_a = 0
for name in x_list:
    for char in name:
        if char == 'a':
            count_a += 1
print("Total occurrences of the letter 'a':", count_a)
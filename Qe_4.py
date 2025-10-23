text=input("enter the line of text:")
x=text.split()
x_cunt={}
for word in x:
    if word in x_cunt:
        x_cunt[word]+=1
    else:
        x_cunt[word]=1
# for word, count in x_cunt.items():
#     print(f"{word}: {count}")
print(x_cunt)
word=input("Enter a word:")
x=word[0]
y=x
for letter in word[1:]:
    if letter == x:
        y += '$'
    else:
        y += letter
print("new word:",y)
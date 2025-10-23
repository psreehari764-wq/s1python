file_name=input("enter the file name:")
parts=file_name.split(".")
if len(parts)>1:
    print("the file extension is:",parts[-1])
else:
    print("no file extension")
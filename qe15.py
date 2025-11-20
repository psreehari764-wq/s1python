class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
l1=int(input("ENTER THE LENGTH OF FIRST RECTANGLE :"))
b1=int(input("ENTER THE BREADTH OF FIRST RECTANGLE :"))
r1=rectangle(l1,b1)
A=r1.area()
P=r1.perimeter()
print("ARAEA OF FIRST RECTANGLE:",A)
print("PERIMETER OF FIRST RECTANGLE:",P)
l2=int(input("ENTER THE LENGTH OF SECOND RECTANGLE :"))
b2=int(input("ENTER THE BREADTH OF SECOND RECTANGLE :"))
r2=rectangle(l2,b2)
a=r2.area()
p=r2.perimeter()
print("ARAEA OF SECOND RECTANGLE:",a)
print("PERIMETER OF SECOND RECTANGLE:",p)


if r1.area()>r2.area():
    print("FIRST RECTANGLE HAS MORE AREA")
else:
    print("SECOND RECTANGLE HAS MORE AREA")
class time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minutes = m
        self.__seconds = s

    def __add__(self, other):
        h = self.__hour + other.__hour
        m = self.__minutes + other.__minutes
        s = self.__seconds + other.__seconds

        if s >= 60:
            m += s // 60
            s = s % 60

        if m >= 60:
            h += m // 60
            m = m % 60

        return time(h, m, s)

    def display(self):
        print("hour:minutes:seconds")
        print(f"{self.__hour}:{self.__minutes}:{self.__seconds}")

h1 = int(input("Enter hours for time 1: "))
m1 = int(input("Enter minutes for time 1: "))
s1 = int(input("Enter seconds for time 1: "))

h2 = int(input("Enter hours for time 2: "))
m2 = int(input("Enter minutes for time 2: "))
s2 = int(input("Enter seconds for time 2: "))

t1 = time(h1, m1, s1)
t2 = time(h2, m2, s2)

t3 = t1 + t2

print("\nResult of addition:")
t3.display()

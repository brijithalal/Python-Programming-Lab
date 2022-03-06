class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        self.area=self.length*self.breadth
        print("Area of the rectangle :",self.area)
    def __lt__(self,second):
        if self.area<second.area:
            return "true"
        else:
            return "false"
print("--- Rectangle 1 ---")
l1=int(input("Enter the length:"))
b1=int(input("Enter the breadth:"))
obj1=rectangle(l1,b1)
obj1.area()
print("--- Rectangle 2 ---")
l2=int(input("Enter the length:"))
b2=int(input("Enter the breadth:"))
obj2=rectangle(l2,b2)
obj2.area()

if obj1<obj2:
    print("\nRectangle 2 is larger than Rectangle 1")
else:
    print("\nRectangle 1 is larger than Rectangle 2")

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

l1=float(input("Enter the length of the rectangle:"))
w1=float(input("Enter the width of the rectangle:"))
l2=float(input("Enter the length of the rectangle:"))
w2=float(input("Enter the width of the rectangle:"))
rect1=Rectangle(l1,w1)2
rect2=Rectangle(l2,w2)
print("Area of rectangle 1 is {} and perimeter is {}:".format(rect1.area(),rect1.perimeter()))
print("Area of rectangle 2 is {} and perimeter is {}:".format(rect2.area(),rect2.perimeter()))
print(rect1.area()>rect2.area())



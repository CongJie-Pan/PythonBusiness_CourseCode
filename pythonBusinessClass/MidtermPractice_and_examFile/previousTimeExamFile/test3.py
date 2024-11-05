class Rectangle():
    def __init__(self,r,c):
        self.r=r
        self.c=c
    def calculate_area(self):
        return self.r*self.c
    def calculate_perimeter(self):
        return (self.r+self.c)*2                   
my_rextangle=Rectangle(5,3)
area=my_rextangle.calculate_area()
perimeter=my_rextangle.calculate_perimeter()
print("The area of the rectangle is",area)
print("The perimeter of the rectangle is :",perimeter)
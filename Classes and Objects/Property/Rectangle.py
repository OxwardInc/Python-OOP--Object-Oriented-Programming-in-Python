class Rectangle():
    def __init__(self, legth, breadth):
        self.length = legth
        self.breadth = breadth
        self.digonal = (self.length*self.length+self.breadth*self.breadth)**0.5

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)
class Product:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display(self):
        print(self._x, self._y)

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self._x = val

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, val):
        self._y = val
    
p = Product(12, 24)


class Person:
    def __init__(self, name, age):
        self.name = name
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError("Age must be between 20 and 80")

    def display(self):
        print(self.name, self._age)

    def set_age(self, new_age):
        if 20 <= new_age <= 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80')
        
    def get_age(self):
        return self._age

if __name__ == '__main__':
    p = Person('Raj', 30)
    p.display()


class Person:
    def __init__(self, name, age):
        self.name = name
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError("Age must be between 20 and 80")

    def display(self):
        print(self.name, self._age)

    @property
    def age(self):
        return self._age
        
    @age.scatter
    def age(self, new_age):
        if 20 <= new_age <= 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80')

if __name__ == '__main__':
    p = Person('Raj', 30)
    p.display()



class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        raise AttributeError("Password not readable")

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._password = new_salary

e = Employee('Jill', 'Feb31', 5000)

class Rectangle():
    def __init__(self, legth, breadth):
        self.length = legth
        self.breadth = breadth
        self.digonal = (self.length*self.length+self.breadth*self.breadth)**0.5

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)
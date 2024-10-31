from Teacher import Teacher
from Student import Student

class Teaching_Assistant(Student, Teacher):
    def greet(self):
        print("Hello, I am a teaching assistant!")

x = Teaching_Assistant()
x.greet()
print(help(Teaching_Assistant))
print(Teaching_Assistant.__mro__)
print(Teaching_Assistant.mro())
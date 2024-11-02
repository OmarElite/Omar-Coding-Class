class Student:
    # Feature
    Grade = 10
    Name = "Omar"

    # Method or Function
    def Introduction(self):
        print("Hi, I am a Student !")

    def Details(self):
        print(f"My name is {self.Name}")
        print(f"I am in Grade {self.Grade}")
    
# Creating a new Object
Obj = Student()
Obj.Introduction()
Obj.Details()

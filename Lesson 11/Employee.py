# Parent Class
class Person():
    def __init__(self, nm, h):
        self.name = nm
        self.age = h


    def Display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age} years old")


# Child Class
class Employee(Person):
    def __init__(self, nm, h, wage, role, id):
        self.idnumber = id
        self.salary = wage
        self.position = role

        # Triggering parent class constractor
        Person.__init__(self, nm, h)


    def Details(self):
        print(f"Salary = {self.salary}")
        print(f"Position = {self.position}")
        print(f"ID Number = {self.idnumber}")


# Creating Object
Obj1 = Employee("Ahmed", 17, 10000, "Manager", "0153458")
Obj1.Display()
Obj1.Details()

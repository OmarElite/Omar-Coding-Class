# Parent Class
class Person():
    def __init__(self, fnm, lnm):
        self.firstName = fnm
        self.lastName = lnm

    
    def printName(self):
        print(f"Full Name = {self.firstName} {self.lastName}")


# Child Class
class Student(Person):
    def __init__(self, fn, ln, year):
        super().__init__(fn, ln)
        self.graduation_year = year


# Creating Objects
Obj1 = Student(" Omar", "Elite", 2030)
Obj1.printName()
print(f"Graduation Year = {Obj1.graduation_year}")

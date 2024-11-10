class Cat:
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

    
    def Info(self):
        print(f"I am a Cat, my Name is {self.name}, and I am {self.age} years old")


    def MakeSound(self):
        print("Miaaou")

    
class Dog:
        
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

    
    def Info(self):
        print(f"I am a Dog, my Name is {self.name}, and I am {self.age} years old")


    def MakeSound(self):
        print("Wouaaff")


# Creating Objects

Obj1 = Cat("Tikky", 12)
Obj2 = Dog("Paul", 14)

for animal in (Obj2, Obj1):
    animal.MakeSound()
    animal.Info()
    print()

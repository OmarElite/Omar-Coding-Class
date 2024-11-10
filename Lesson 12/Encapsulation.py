
class Computer:
    def __init__(self):
        self.__MaximumPrice = 900
        self.MinimumPrice = 100
        

    def Selling(self):
        print(f"The Minimum Price is : {self.MinimumPrice}")
        print(f"The Selling Price = {self.__MaximumPrice}")


    def SetMaximumPrice(self, Price):
        self.__MaximumPrice = Price


Obj1 = Computer()
Obj1.Selling()
print()

# Trying to change the MAXIMUM price outside the Class
Obj1.__MaximumPrice = 500  
Obj1.MinimumPrice = 250   # <---
print("After trying to update Maximum selling Price outside of the Class")
Obj1.Selling()
print()

# Trying to change the Maximum Price inside of the Class
Obj1.SetMaximumPrice(500)
print("After trying to update Maximum selling Price inside of the Class by accessing the methode")
Obj1.Selling()
print()

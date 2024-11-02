class Parrot:
    # Class Feature
    Species = "Bird"

    # Instence Attribute
    def __init__(self, color, nm, old):
        self.bird_color = color
        self.name = nm
        self.age = old


# creating a New object
Obj1 = Parrot("Blue", "Flappy", 10)
Obj2 = Parrot("Black", "Eagle", 12)

# Access The class Attribute
print(f"{Obj1.name} is a {Obj1.Species}")
print(f"{Obj2.name} is a {Obj2.Species}")
print()

# Access the Instance Attribute
print(f"{Obj1.name} has {Obj1.bird_color} color and it is {Obj1.age} years old")
print(f"{Obj2.name} has {Obj2.bird_color} color and it is {Obj2.age} years old")

class Robot:
    Species = "Robot"

    def __init__(self, cl, nm, old):
        self.color = cl
        self.name = nm
        self.age = old


Tom = Robot("Blue", "Tom", 17)
Jerry = Robot("Red", "Jerry", 12)

print(f"{Tom.name} is a {Tom.Species}")
print(f"{Jerry.name} is a {Jerry.Species}")
print()

print(f"{Tom.name} has {Tom.color} color and it is {Tom.age} years old")
print(f"{Jerry.name} has {Jerry.color} color and it is {Jerry.age} years old")
print()

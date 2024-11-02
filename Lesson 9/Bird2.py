class Bird:
    # Instance Attribute
    def __init__(self, color, nm, old):
        self.bird_color = color
        self.bird_name = nm
        self.bird_age = old


    # Instance method
    def sing(self, song):
        return f"{self.bird_name} love to Sing {song}"


# Creating the Object

obj1 = Bird("Red", "Ali", 13)
print(obj1.sing("'My Life'"))

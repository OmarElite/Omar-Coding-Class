class employee:
    # Initializing the Constractor
    def __init__(self, nm, r):
        self.name = nm
        self.role = r
        print("Employee created")

    # Deleting the object or Destractor
    def __del__(self):
        print("Destructor called Employee is Deleted")


# Creating the object
obj1 = employee("Omar", "Student")
del obj1

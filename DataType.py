name = "Omar" #str
age = 15 #int
weight = 50.4 #float
isStudent = True #bool

print(f"My name is {name}")
print(f"Data Type of Name is {type(name)}")
print()

print(f"I am {age} years old")
print(f"Data Type of Age is {type(age)}")
print()

print(f"I am {weight} kg")
print(f"Data Type of Weight is {type(weight)}")
print()

print(f"Am I a student ? {isStudent}")
print(f"Data Type of Student is {type(isStudent)}")
print()

# Type Cafting

print("After Type Cafting")
age = str(age)
print(f"Data Type of Age is {type(age)}")
print()

weight = int(weight)
print(f"Data Type of Weight is {type(weight)}")
print()

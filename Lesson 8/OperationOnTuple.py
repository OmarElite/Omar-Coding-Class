MyTuple = ("Apple", "Orange", "Banana")
print(f"My Tuple = {MyTuple}")
print()

# Tuple with mix Data Types
MyTuple_2 = (7, 1.2, "Car", True)
print(f"My Tuple number 2 = {MyTuple_2}")
print()

# Nested Tuple
MyTuple_3 = ("Banana", (5, "Tree", 2.7, False), 9)
print(f"My Tuple number 3 = {MyTuple_3}")
print(f"The first Data of My Tuple 3 is '{MyTuple_3[0]}'")
print()
print(f"The second Data of My Tuple 3 is {MyTuple_3[1]}")
print()
print(f"SubData of the Second element of My Tuple 3 is '{MyTuple_3[1][0]}'")
print()
print(f"SubData of the Second element of My Tuple 3 is '{MyTuple_3[1][2]}'")
print()

# Slicing
Fruit_Tuple = ("Apple", "Orange", "Banana", "Kiwi", "Mango", "Watermelon", "Strawberry", "Pineapple", "Grape", "Coco")
print(Fruit_Tuple)
print(f"The first Five Fruits = {Fruit_Tuple[0:5]}")
print()

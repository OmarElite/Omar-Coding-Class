MySet = {"Mango", "Apple", "Apple", "Apple", "Orange"}
print(f"My Set = {MySet}")
print()

# Adding new elements in the Set
MySet.add("Banana")
print(f"My Updated Set = {MySet}")
print()

# The deference of two Sets
Set_1 = {"Mango", "Apple", "Orange"}
Set_2 = {"Mango", "Grape", "Watermelon"}
print("The element in the Set 1 that is not available in the Set 2")
print(Set_1.difference(Set_2))
print()

print("The element in the Set 2 that is not available in the Set 1")
print(Set_2.difference(Set_1))
print()

# Symetric difference
print("Symetric difference")
print(Set_1.symmetric_difference(Set_2))

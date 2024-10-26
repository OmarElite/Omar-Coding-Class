Fruit_List = ["Apple", "Banana", "Watermelon", "Kiwi", "Orange"]

print(f"Original List : {Fruit_List}")
print()
print(f"Len of the list = {len(Fruit_List)}")
print()

print(f"The first element of the list is the {Fruit_List[0]}")
print(f"The last element of the list is the {Fruit_List[4]}")
print()

# Adding new elements in the list
Fruit_List.append("Mango")
print(f"Updated List : {Fruit_List}")
print()

# Adding element in a specific index
Fruit_List.insert(0, "Strawberry")
print(f"Updated List : {Fruit_List}")
print()

# Surting the list in Ascending order
Fruit_List.sort()
print(f"Surted list = {Fruit_List}")
print()

# Sorting the List in descending order
Fruit_List.reverse()
print(f"Reversed list : {Fruit_List}")
print()

# Removing the element directily without knowing the index number
Fruit_List.remove("Watermelon")
print(f"Updated list after removing Watermelon : {Fruit_List}")
print()

# Removing the elements by the index number 
Fruit_List.pop(1)
print(f"Updated list after removing the data in the index 1 : {Fruit_List}")
print()

# Displaying the fisrt two elements of the list
Fruit_List_2 = Fruit_List[0:2]
print(f"The fisrt two elements of the list are {Fruit_List_2} ")
print()

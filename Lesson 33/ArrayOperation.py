myList = [14, "apple", 5.41, True]

print("Original List :")
print(myList)

print(f"The length of my List is {len(myList)}")
print()

# And elements at the end of the List
myList.append(45)
print(f"Updated list after adding new elements :")
print(myList)
print()

# And elements at specific position
myList.insert(2, "Tomato")
print(f"Updated list after adding new elements at the index 2 : ")
print(myList)
print()

# Remove the last elements from the list
myList.pop()
print("Updated list after removing the last element : ")
print(myList)
print()

# Remove the element based on the index
myList.pop(1)
print("Updated list after removing element in the index 1 : ")
print(myList)
print()

# Remove the element based on the data it self
myList.remove("Tomato")
print("Updated list after removing the element itself without the index : ")
print(myList)
print()

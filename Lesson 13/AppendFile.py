# Combining File Content from 1 file to other File
# Open Both Files in Read mode
First_file = open("Sample1.txt", "r")
Second_file = open("Sample2.txt", "r")

# Print the original content of both files
print("Original content of Sample1.txt before appending")
print(First_file.read())
print()

print("Original content of Sample2.txt before appending")
print(Second_file.read())
print()

First_file.close()
Second_file.close()

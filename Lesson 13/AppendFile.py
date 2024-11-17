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

# Open first file and Second file in Append mode
First_file = open("Sample1.txt", "a+")
Second_file = open("Sample2.txt", "r")

# Updating first file Content with the second file content
First_file.write("\n")
First_file.write(Second_file.read())

# Relocating the Cursor of the File at the Begining
First_file.seek(0)
Second_file.seek(0)

# Displaying the updated contents after appending process
print("Content of Sample1.txt after appending :")
print(First_file.read())
print()

print("Content of Sample2.txt after appending :")
print(Second_file.read())
print()


First_file.close()
Second_file.close()

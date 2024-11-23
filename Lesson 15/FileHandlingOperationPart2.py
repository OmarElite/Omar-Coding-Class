import os

# Create a new empty file 
new_file = open("Sample5.txt", "x")
new_file.close()

# Check weather the file exist
if os.path.exists("Sample5.txt"):
    os.remove("Sample5.txt")
    print("file exist and already been removed")
else:
    print("The file does not exist")

# Delete the folder if it's exist
if os.path.exists("Folder1"):
    os.rmdir("Folder1")
    print("Folder1 already been removed")

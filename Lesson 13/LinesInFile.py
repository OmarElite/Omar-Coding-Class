# Open the File in Read mode
f = open("Sample2.txt", "r")
counter = 0

# Read the File content and Store them into a Variable
content = f.read()

# Spliting contents into lines and storing them in a list
content_list = content.split("\n")

for i in content_list:
    print(i)
    counter = counter+1

print()
print(f"Total lines in the File 'Sample2.txt' is : '{counter}'")
print()

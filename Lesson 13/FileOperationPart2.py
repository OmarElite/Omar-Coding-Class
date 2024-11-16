# Open the File in Read mode
f_read = open("Sample1.txt", "r")

# Displaying the Content
print("File in Read mode")
print("Original File Content : ")
print(f_read.read())

# Close the File
f_read.close()
print()
print()

# Open the file in Write mode
f_write = open("Sample1.txt", "w")

# Rewriting the File Content
f_write.write("Hello, I am a Student ")
f_write.write(" My name is Omar, I am 15 years old")

# Colse the File
f_write.close()

# Open the File in Read mode after rewriting the Content
f_updated = open("Sample1.txt", "r")
print("File in Read mode")
print("Updated File Content : ")
print(f_updated.read())

f_updated.close()

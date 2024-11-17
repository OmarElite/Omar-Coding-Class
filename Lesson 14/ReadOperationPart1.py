# Open file and read all of it's content
f = open("Sample1.txt", "r")

print("All of the Sample1.txt Contents :")
print(f.read())
print()

# Relocating the Cursor
f.seek(0)

# Read the first 10 characters
print("The first 10 characters of Sample1.txt :")
print(f.read(10))

f.close()
print()

# Reading the original content of Sample2.txt
f2 = open("Sample2.txt", "r")
print("Original Content of Sample2.txt :")
print(f2.read())
print()

f2.close()

# Append manualy on one File
f2 = open("Sample2.txt", "a")
f2.write("\nI study in the First Grade of HighSchool")

f2.close()

# Reading the Updated Content of Smple2.txt
f2 = open("Sample2.txt", "r")
print("Updated Content of Sample2.txt :")
print(f2.read())
print()

f2.close()

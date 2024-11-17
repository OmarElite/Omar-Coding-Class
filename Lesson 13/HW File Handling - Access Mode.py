# File Content 'Fonction'
def File_Content():
    f_w.write("\n")
    f_w.write("Introduction of Class 8 students:\n")
    f_w.write("\n")
    f_w.write("Number of Students: 25\n")
    f_w.write("Students favorite subject: Mathematiques\n")
    f_w.write("Class Monitor: Roy\n")
    f_w.write("Teacher's Name: Elena\n")
    f_w.write("\n")

# Open the File in Read Mode
f_r = open("HW.txt", "r")
print(f_r.read())

# Open the File in Write Mode
f_w = open("HW.txt", "w")

# Calling the Fonction
File_Content()

# Close the two Modes
f_w.close()
f_r.close()

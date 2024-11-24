from tkinter import *

window = Tk()
window.title("Grid Position")
window.geometry("480x360")

# Creating Widget
Label1 = Label(text="Hello", fg="Black", bg="white")
Label2 = Label(text="My name is Omar", fg="Black", bg="white")
Label3 = Label(text="I am 15 years old", fg="Black", bg="white")

Button1 = Button(fg="Black", bg="white", text="Enter", width=8, height=2)

# Positioning using Grid
Label1.grid(row=0, column=0, padx=5, pady=5)
Label2.grid(row=0, column=1, padx=5, pady=5)
Label3.grid(row=0, column=2, padx=5, pady=5)
Button1.grid(row=1, column=1, pady=5)

window.mainloop()
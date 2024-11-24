from tkinter import *

# Creating window
window = Tk()
window.title("Sample Title")
window.geometry("400x300") # Side of the window : The width is 400 and Height is 300

# Creating widgets
# Label
Label1 = Label(text="Hello World", fg="Black", bg="white")

# Entry or text input
Entry1 = Entry(fg="Black", bg="white", width=30)

# Crating button
Button1 = Button(fg="Black", bg="white", text="Ok")

# Displaying the Widget on the window
Label1.pack()
Entry1.pack()
Button1.pack()

window.mainloop()
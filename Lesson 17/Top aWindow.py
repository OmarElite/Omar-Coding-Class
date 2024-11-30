from tkinter import *

window = Tk()
window.title("Top a Window")
window.geometry("400x300")

def topwin():
    # Setting up top window
    top = Toplevel()
    top.title("Top Level")
    top.geometry("300x200")

    # Creating widgets for top Window
    Label2 = Label(top, text="This is top Level Window")
    Label2.pack()

    top.mainloop()

# Creating widget
Label1 = Label(window, text="This is Main Window")
Button1 = Button(window, text="Click here to Open another Window", command=topwin)

# Displaying the Widget
Label1.pack()
Button1.pack()

window.mainloop()
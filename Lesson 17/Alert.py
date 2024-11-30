from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Message Box")
window.geometry("400x300")

def msg():
    messagebox.showerror("Alert", "Stop, Virus Found !")


# Creating Button
Button1 = Button(window, text="Scan for Virus", bg= "White", fg="Black", command=msg)

# Displaying the Button on the Window
Button1.place(x=100, y=100)



window.mainloop()
from tkinter import *
from PIL import Image, ImageTk

# Creating the Window 
window = Tk()
window.title("Image")
window.geometry("400x300")

# Open the image file
Upload = Image.open("Omar-Palestine-Image.png")

# Converte imgae into Tkinter compatible image
img = ImageTk.PhotoImage(Upload)

# Creating label and add the image into the label
Label1 = Label(window, image=img, height=200, width=200)
Label2 = Label(window, text="Sample Photo")

# Displaying the widget on the window
Label1.place(x=50, y=20)
Label2.place(x=50, y=250)

window.mainloop()
import turtle as t

# Creating the Canvas or the drawing book
sc = t.Screen()
sc.bgcolor("White")
sc.setup(500, 500) # Canvas Size
t.title("drawing a Ranbow spiral")

# Making a Pen
pen = t.Turtle()

# Preparing the color
color = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink"]

while True:
    for i in range(200):
        pen.pencolor(color[i%len(color)])
        pen.width(i/100 + 1)
        pen.forward(i)
        pen.left(59)

    pen.right(239)

    for i in range(200, 0, -1): 
        pen.pencolor("Black")
        pen.width(i/100 + 7)
        pen.forward(i)
        pen.left(59)


t.done()

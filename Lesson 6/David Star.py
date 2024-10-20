import turtle as t

# Creating the Canvas or the drawing book
sc = t.Screen()
sc.bgcolor("Green")
sc.setup(500, 500) # Canvas Size
t.title("drawing a David Star")

# Making a Pen
pen = t.Turtle()

# Drawing a David Star
# Drawing The first Triangle

pen.pendown() # Pen facing down so we can draw
for i in range(3):
    pen.forward(100)
    pen.left(120)

# Moving the pen position without drawing
pen.penup() # Pen facing up so we can move without drawing
pen.right(30)
pen.forward(50)

# Drawing the second triangle
pen.pendown() # Pen facing down so we can draw
pen.left(90)

for i in range(3):
    pen.forward(100)
    pen.left(120)


t.done()

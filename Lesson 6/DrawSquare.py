import turtle as t

# Creating the Canvas or the drawing book
sc = t.Screen()
sc.bgcolor("Blue")
sc.setup(500, 500) # Canvas Size
t.title("drawing a square")

# Make the Pen
pen = t.Turtle()

# Drawing a Square
for i in range(4):
    pen.forward(200)
    pen.left(90)

t.done()


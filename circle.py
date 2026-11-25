import math

def drawCircle(turtle, x, y, radius):
    distance = 2.0 * math.pi * radius / 120.0

    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()

    for i in range(120):
        turtle.forward(distance)
        turtle.left(3)

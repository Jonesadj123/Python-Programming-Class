import turtle

def koch(turtle, length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length = length / 3.0

        koch(turtle, length, level - 1)
        turtle.left(60)

        koch(turtle, length, level - 1)
        turtle.right(120)

        koch(turtle, length, level - 1)
        turtle.left(60)

        koch(turtle, length, level - 1)


def drawKochSnowflake(turtle, length, level):
    for i in range(3):
        koch(turtle, length, level)
        turtle.right(120)


# Create the turtle
myTurtle = turtle.Turtle()
myTurtle.speed(0)

# Draw the Koch snowflake
drawKochSnowflake(myTurtle, 300, 2)

turtle.done()

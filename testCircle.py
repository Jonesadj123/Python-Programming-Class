import turtle
import sys

sys.path.append("C:/Users/jones/Downloads")

from circle import drawCircle

myTurtle = turtle.Turtle()
drawCircle(myTurtle, 0, 0, 100)

turtle.done()

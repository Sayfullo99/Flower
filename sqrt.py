import turtle
import math
import random

bob = turtle.Turtle()
turtle.colormode(180)
bob.speed(1000)

for i in range(2000):
	bob.forward(math.sqrt(i))
	bob.left(i%180)

turtle.done()
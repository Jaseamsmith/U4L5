from turtle import *

charlie = Turtle()
charlie.color("blue")
charlie.pensize(3)
charlie.speed(3)
charlie.shape("turtle")

def drawstar():
	for x in range(5):
		charlie.forward(50)
		charlie.left(144)

drawstar()

mainloop()
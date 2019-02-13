from turtle import *

charlie = Turtle()

charlie.color("pink")
charlie.pensize(3)
charlie.speed(0)
charlie.shape("turtle")

def drawstar():
	for x in range(5):
		charlie.forward(50)
		charlie.left(144)

for y in range(2):
	drawstar()
	charlie.penup()
	charlie.forward(50)
	charlie.pendown()

drawstar()

mainloop()
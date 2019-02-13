from turtle import *

charlie = Turtle()

charlie.color("blue")
charlie.pensize(3)
charlie.speed(0)
charlie.shape("turtle")

def drawhex(side):
	for x in range(6):
		charlie.forward(side)
		charlie.left(60)

for y in range(25,150,25):
	drawhex(y)

mainloop()
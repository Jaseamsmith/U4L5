from turtle import *

charlie = Turtle()

charlie.color("blue")
charlie.pensize(5)
charlie.speed(0)
charlie.shape("turtle")

def drawtriangle():
	for x in range(3):
		charlie.forward(100)
		charlie.left(120)

drawtriangle()

for x in range(12):
	drawtriangle()
	charlie.left(30)

mainloop()
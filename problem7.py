from turtle import *

charlie = Turtle()

charlie.color("purple")
charlie.pensize(3)
charlie.speed(0)
charlie.shape("turtle")

def drawstar():
	for x in range(5):
		charlie.forward(50)
		charlie.left(144)

def row():
	for y in range(3):
		drawstar()
		charlie.penup()
		charlie.forward(60)
		charlie.pendown()

for z in range(4):
	row()
	charlie.penup()
	charlie.backward(180)
	charlie.right(90)
	charlie.forward(60)
	charlie.left(90)
	charlie.pendown()

mainloop()

#charlie.write('hello Jaseam')
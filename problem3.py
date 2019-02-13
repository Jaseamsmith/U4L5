from turtle import *

 charlie = Turtle()

charlie.color("blue")
charlie.pensize(5)
charlie.speed(5)
charlie.shape("turtle")

for x in range(6):
	charlie.forward(100)
	charlie.left(60)

mainloop()
import turtle

t = turtle.Pen()
sides = int(turtle.numinput("Input sides", "Please input number of sides (3~10)", 4, 3, 10))
for i in range(sides):
    t.forward(50)
    t.left(360/sides)

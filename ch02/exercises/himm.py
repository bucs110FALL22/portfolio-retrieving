import turtle

CIRCLE_DEG = 360

wn = turtle.Screen()
wn.setup(400, 400)
him = turtle.Turtle()

sides = 4
length = 50


colors = ["red", "purple", "blue"]

for c in colors:  
  him.color(c)

for i in range (sides):
  him.left(CIRCLE_DEG/sides)
  him.forward(length)

him.up()
him.forward(100)
him.down()

wn.exitonclick()



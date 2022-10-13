
import turtle
def drawEQShape():
  him = turtle.Turtle()
  him.shape = ("turtle")
  him.color = ("green")
  sl = int(input("Length of the sides: "))
  num_of_sides = int(input("Number of sides: "))
  angle = 360 /num_of_sides
  for i in [angle]*num_of_sides:
    him.forward(sl)
    him.left(i) 

drawEQShape()
turtle.done()
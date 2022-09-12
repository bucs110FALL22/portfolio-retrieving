import turtle

wn = turtle.Screen()
him = turtle.Turtle()

him.color("Purple")

CIRCLE_DEG = 360

number_of_sides = input("How many sides: ")
length_of_each_side = []
for i in range (int(number_of_sides)): 
  length_of_each_side.append(input("Length of "+str(i+1)))

for i in range (int(number_of_sides)):
  him.left(CIRCLE_DEG/int(number_of_sides))
  him.forward(int(length_of_each_side[i]))

him.up()
him.forward(100)
him.down()

wn.exitonclick()
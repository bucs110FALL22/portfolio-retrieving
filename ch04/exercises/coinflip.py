import turtle
import random
him = turtle.Turtle()
wn = turtle.Screen()

def flip_coin():
    return random.choice(["heads", "tails"])
print(flip_coin())

def isInScreen(w,u):
    leftBound = - w.window_width() / 4
    rightBound = w.window_width() / 4
    topBound = w.window_height() / 4
    bottomBound = -w.window_height() / 4
  

    turtleX = u.xcor()
    turtleY = u.ycor()

    twt = True
    if turtleX > rightBound or turtleX < leftBound:
        twt = False
    if turtleY > topBound or turtleY < bottomBound:
       twt = False

    return twt


him.shape('turtle')
while isInScreen(wn,him):
    tt = random.randrange(0, 4)
    if tt == 0:
        him.left(90)
    else:
        him.right(90)

    him.forward(50)

wn.exitonclick()

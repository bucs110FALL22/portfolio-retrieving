import turtle

def Constants():
  return '#D71E22', '#ADD8E6', '#FAE599'

def Body(color): 
  
    PEN.pensize(10)
    PEN.speed(5)
    PEN.fillcolor(color)
    PEN.begin_fill()
    PEN.up()
    PEN.backward(50)
    PEN.down()
    PEN.left(90)
    PEN.forward(70)
    PEN.right(90)
    PEN.forward(150)
    PEN.right(90)
    PEN.forward(200)
    PEN.right(90)
    PEN.forward(50)
    PEN.right(90)
    PEN.forward(30)
    PEN.left(90)
    PEN.forward(50)
    PEN.left(90)
    PEN.forward(30)
    PEN.right(90)
    PEN.forward(50)
    PEN.right(90)
    PEN.forward(130)
    
    PEN.end_fill()

def Eyeglass(color): 
  
    PEN.pensize(10)
    PEN.speed(5)
    PEN.fillcolor(color)
    PEN.begin_fill()
    PEN.up()
    PEN.right(90)
    PEN.forward(45)
    PEN.down()
    PEN.left(90)
    PEN.forward(40)
    PEN.right(90)
    PEN.forward(100)
    PEN.right(90)
    PEN.forward(40)
    PEN.right(90)
    PEN.forward(100)
    PEN.end_fill()

def Backpack(color):

    PEN.pensize(10)
    PEN.speed(5)
    PEN.fillcolor(color)
    PEN.begin_fill()
    PEN.up()
    PEN.forward(50)
    PEN.right(90)
    PEN.forward(15)
    PEN.down()
    PEN.left(90)
    PEN.forward(50)
    PEN.left(90)
    PEN.forward(80)
    PEN.left(90)
    PEN.forward(50)
    PEN.left(90)
    PEN.forward(80)
    PEN.end_fill()

def Hat(color):
    PEN.pensize(10)
    PEN.speed(5)
    PEN.fillcolor(color)
    PEN.begin_fill()
    PEN.up()
    PEN.forward(55)
    PEN.down()
    PEN.left(90)
    PEN.forward(20)
    PEN.right(160)
    PEN.forward(100)
    PEN.right(40)
    PEN.forward(100)
    PEN.right(160)
    PEN.forward(167)
    PEN.end_fill()
if __name__ == "__main__": 
  AMONGUS_RED, AMONGUS_EYEGLASS, AMONGUS_HAT = Constants()
  SCREEN = turtle.getscreen()
  PEN = turtle.Turtle()
  Body(AMONGUS_RED)
  Eyeglass(AMONGUS_EYEGLASS)
  Backpack(AMONGUS_RED)
  Hat(AMONGUS_HAT)
  PEN.screen.exitonclick()
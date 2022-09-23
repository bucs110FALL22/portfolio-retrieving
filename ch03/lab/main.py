import turtle #1. import modules

from random import randint
import pygame
import math
#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

x = randint(1,100)
print("MichelAngelo moves forward ", x)
michelangelo.forward(x)
x = randint(1,100)
print("Leonardo moves forward ", x)
leonardo.forward(x)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for loop_increment_variable in range(10):
  x = randint(0,10)
  michelangelo.forward(x)
  print("MichelAngelo moves forward ", x)
  x = randint(0,10)
  leonardo.forward(x)
  print("Leonardo moves forward ", x)

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()


def drawshape(numOfSides, sideLength, offset ):
  coords = []
  ORANGE = (155,100,0)
  for loop_increment_variable in range(numOfSides):
    theta = (2.0 * math.pi * loop_increment_variable) / numOfSides
    x = sideLength * math.cos(theta) + offset
    y = sideLength * math.sin(theta) + offset
    coords.append((x,y))
  pygame.draw.polygon(window , ORANGE, coords)
  pygame.display.flip()
  pygame.time.wait(1000)

OFF_SET = 100
SIDE_LENGTH = 100
drawshape(3, SIDE_LENGTH, OFF_SET)
drawshape(4, SIDE_LENGTH, OFF_SET)
drawshape(6, SIDE_LENGTH, OFF_SET)
drawshape(9, SIDE_LENGTH, OFF_SET)
drawshape(360, SIDE_LENGTH, OFF_SET)

window.exitonclick()
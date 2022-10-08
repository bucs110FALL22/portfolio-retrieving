import pygame
import random
import math
Loop1 = True
BLUE = (0, 0, 255)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (118,238,0)
ORANGE = (255,153,18)
WIDTH = 400
LENGTH = 400
gameDisplay = pygame.display.set_mode((WIDTH,LENGTH))
gameDisplay.fill(BLUE)
DARTX = 0
DARTY = 0
DARTR = 3

guess = 1
def setup2():
  pygame.draw.circle(gameDisplay, ORANGE, (200,200), 200)
  pygame.draw.line(gameDisplay,BLACK,(200,0),(200,400),2)
  pygame.draw.line(gameDisplay,BLACK,(0, 200),(400, 200),2)
  
def clickevent():
   
    if pygame.mouse.get_pressed(3)[0]:
          print("clicked")
          pos = pygame.mouse.get_pos()
          print(pos)
          if pos[0]<200: 
            guess = 1
            print("You have chosen Player 1")
          else: 
            guess = 2
            print("You have chosen Player 2")
          return False
    else:
      return True

      
def guesswhichonewon():
  pygame.draw.rect(gameDisplay, RED, pygame.Rect(0, 0, 200, 400))
  print("Click red for player one, Click blue for player two")
def singleshot(PLAYER, COLORHIT, COLORMISS):
    DARTX = random.randrange(0, 400)
    DARTY = random.randrange(0, 400)
    distance_from_center = math.hypot(DARTX-200, DARTY-200)
    is_in_circle = distance_from_center <= WIDTH/2
    if is_in_circle:  
      pygame.draw.circle(gameDisplay, COLORHIT, (DARTX, DARTY), DARTR)
      print(PLAYER + "hit")
      return 1
    else: 
      print(PLAYER + "miss")
      pygame.draw.circle(gameDisplay, COLORMISS, (DARTX, DARTY), DARTR)
      return 0
def shoot():
  player1score = 0
  player2score = 0
  for i in range (10):  
    print("round ", i + 1)
    player1score += singleshot("player 1", RED, ORANGE)
    print("Player 1 score is: ", player1score)
    player2score += singleshot("Player 2", BLUE, BLACK)
    print("Player 2 score is: ", player2score)
  if player1score > player2score: 
    print("Player 1 Wins! Their score was ", player1score)
    if guess == 1: 
      print("You guessed correctly!")
    else: 
      print("You guessed wrong.")
  elif player1score < player2score: 
    print("Player 2 Wins! Their score was ", player2score)
    if guess == 2: 
      print("You guessed correctly!")
    else: 
      print("You guessed wrong.")
  else: 
    print("Tie!\n L bozo")
if __name__ == "__main__":
  pygame.init()
  guesswhichonewon()
  pos = (0,0)
  while Loop1:
    for event in pygame.event.get():
      Loop1 = clickevent()
      if event.type == pygame.QUIT:
          pygame.quit()
          quit()
    pygame.display.update()
  
  setup2()
  shoot()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          quit()
    pygame.display.update()

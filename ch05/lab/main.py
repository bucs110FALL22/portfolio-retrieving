from collections import defaultdict
import pygame
def algorithm(n): 
  count = 0
  while n > 1: 
    if n % 2 == 0: 
      n /= 2
    else: 
      n = 3 * n + 1
    print (n)
    count += 1
  return count
def makedict(upper_Limit):
  max_val = 0
  upper_limit = upper_Limit
  lower_limit = 2
  iters = {}
  real_iters = []
  max_x = 0
  iters = defaultdict(list)
  for i in range (lower_limit,upper_limit):
    if algorithm (i) > max_val: 
      max_val = algorithm (i)
      max_x = i
    iters [(i)].append((algorithm(i)))
    real_iters.append((int(i), int(algorithm(i)))) 
  return iters , max_val, real_iters, max_x
if __name__ == "__main__":
  pygame.init()
  pygame.display.init()
  upper_limit = 20
  lower_limit = 2
  iters, max_val, real_iters, max_x = makedict(upper_limit)
  max_so_far = 0
  scale = 15
  AQUA = (0, 255, 255)
  scale_iters = [(x * scale, y * scale) for x, y in real_iters]
  BLACK = (255, 255, 255)
  display = pygame.display.set_mode((400,400))
  font = pygame.font.Font(None, 20)
  pygame.draw.lines(display, BLACK, False, scale_iters)
  new_display = pygame.transform.flip(display, False, True)
  display.blit( new_display , (0, 0) )
  message = "Maximum value at "+ str((max_x, max_val))
  msg = font.render(message, True, BLACK)
  display.blit(msg, (0,0))
  pygame.display.update()

  
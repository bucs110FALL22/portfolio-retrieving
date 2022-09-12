import pygame

pygame.init()

#gets the display and makes it full screen
#no arguements means full screen
screen = pygame.display.set_mode()

#RGB Scheme
#[R, G, B] -> [0-255, 0-255, 0-255]
screen.fill([255, 0, 0])
pygame.display.flip()
pygame.time.wait(500)
screen.fill([0, 255, 0])
pygame.display.flip()
pygame.time.wait(500)

screen.fill([0, 0, 255])
pygame.display.flip()
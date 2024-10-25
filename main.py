from cards import *
from hand import *

import ctypes, pygame, sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_LENGTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()




def Game():
    print()


"""
if __name__ == "__main__":
    game = Game()
    game.run()
    """
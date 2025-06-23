import sys

import pygame

from game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game(600, 400)
    game.run()
    pygame.quit()
    sys.exit()

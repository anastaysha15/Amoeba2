import pygame
from game import Game
from menu import menu

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    g = Game(screen)

    t = menu(g)
    while t is not False:
        t = g.game(t)
        t = t and menu(g)

    pygame.quit()

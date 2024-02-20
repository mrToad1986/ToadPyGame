import pygame
from common import const
from common import variables


pygame.init()
pygame.display.set_caption(const.GAME_TITLE)
screen = pygame.display.set_mode(const.WIN_SIZE)
screen.fill(variables.bg_color['серо-зеленый'])
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
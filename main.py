import pygame
from common import const
from common import variables


pygame.init()
pygame.display.set_caption(const.GAME_TITLE)
screen = pygame.display.set_mode(const.WIN_SIZE)
screen.fill(variables.bg_color['серо-зеленый'])

#фоновое изображение
background_image = pygame.image.load("img/bg1.png")
background_image = pygame.transform.scale(background_image, const.WIN_SIZE)
screen.blit(background_image, (0,0))


done = False
# переписать через while true и вынести flip из цикла?
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
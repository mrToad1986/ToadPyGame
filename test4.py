import pygame
import math

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("геометрические фигуры")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
pink = (255, 192, 203)
yellow_mellon = (244,169,0)
sm_green = (119, 221, 119)

circle_x = screen_width/2
circle_y = screen_height/2
circle_radius = 50
pygame.draw.circle(screen, yellow_mellon, (circle_x, circle_y), circle_radius)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    circle_x += 1
    pygame.display.update()
    pygame.time.Clock().tick(12)

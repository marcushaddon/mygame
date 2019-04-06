"""Run game."""
import pygame

from player import Player

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

white = 255, 255, 255

player = Player('assets/circle.png')

screen.blit(player.img, (0,0))

clock = pygame.time.Clock()

while True:
    clock.tick(60)


    screen.fill(white)
    screen.blit(player.img, player.rect)
    pygame.display.flip()

    player.draw()

    pygame.event.pump()
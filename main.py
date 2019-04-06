"""Run game."""
import pygame

from game import Game
from player import Player

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

game = Game(screen)

player = Player('assets/circle.png')

game.spawn(player, (34, 34))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    game.draw()
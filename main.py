"""Run game."""
import pygame

from game import Game
from game_object import GameObject
from player import Player

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

game = Game(screen)

player = Player('assets/circle.png')
ball = GameObject('assets/circle.png')

game.spawn(ball, (50, 50))
game.spawn(player, (width / 2, height / 2))


clock = pygame.time.Clock()

while True:
    clock.tick(60)
    game.draw()
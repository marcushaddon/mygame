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
ball = GameObject('assets/ball.jpeg')

game.spawn(ball)
game.spawn(player, (100, 134))


clock = pygame.time.Clock()

while True:
    clock.tick(60)
    game.draw()
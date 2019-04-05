"""Run game."""
import pygame

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)

black = 0, 0, 0

player = pygame.image.load('assets/circle.png')
playerbox = player.get_rect()

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    left, up, right, down = (
        keys[pygame.K_LEFT] or keys[pygame.K_a],
        keys[pygame.K_UP] or keys[pygame.K_w],
        keys[pygame.K_RIGHT] or keys[pygame.K_d],
        keys[pygame.K_DOWN] or keys[pygame.K_s],
    )

    if playerbox.left < 0:
        left = 0
    
    if playerbox.right > width:
        right = 0
    
    if playerbox.top < 0:
        up = 0

    if playerbox.bottom > height:
        down = 0
    
    playerbox = playerbox.move((
        right - left,
        down - up,
    ))
    screen.fill(black)
    screen.blit(player, playerbox)
    pygame.display.flip()

    pygame.event.pump()
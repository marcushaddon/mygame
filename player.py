"""Module for player related code."""
from typing import List

import pygame

class Player(object):
    """Class for implementing the player object."""

    def __init__(self, img: str):
        """Initialize player object."""
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
    
    def draw(self):
        """Process tick of event loop."""
        # Get keyboard input
        keys = pygame.key.get_pressed()
        left, up, right, down = (
            keys[pygame.K_LEFT] or keys[pygame.K_a],
            keys[pygame.K_UP] or keys[pygame.K_w],
            keys[pygame.K_RIGHT] or keys[pygame.K_d],
            keys[pygame.K_DOWN] or keys[pygame.K_s],
        )

        self.rect = self.rect.move((
            right - left,
            down - up,
        ))

    def move(self, vector: List[int]) -> None:
        """Move player."""
        # TODO: Check for collisions
        self.rect = self.rect.move(vector)
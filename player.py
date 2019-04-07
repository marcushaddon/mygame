"""Module for player related code."""
from typing import List

import pygame

from game_object import GameObject

class Player(GameObject):
    """Class for implementing the player object."""

    def __init__(self, img: str):
        """Initialize player object."""
        GameObject.__init__(self, img)
    
    def next(self) -> None:
        """Process tick of event loop."""
        super().next()
        # Get keyboard input
        keys = pygame.key.get_pressed()
        left, up, right, down = (
            keys[pygame.K_LEFT] or keys[pygame.K_a],
            keys[pygame.K_UP] or keys[pygame.K_w],
            keys[pygame.K_RIGHT] or keys[pygame.K_d],
            keys[pygame.K_DOWN] or keys[pygame.K_s],
        )

        self.move((
            right - left,
            down - up,
        ))

    def move(self, vector: List[int]) -> None:
        """Move player."""
        # TODO: Check for collisions
        self.rect = self.rect.move(vector)
    
    def on_collision_enter(self, other: GameObject) -> None:
        """Handle collision enter."""
        print("DO YOU NOW HOW I HAVE")
        GameObject.on_collision_enter(self, other)
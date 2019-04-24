"""Module for player related code."""
from typing import List

import pygame

from game_object import GameObject

class Player(GameObject):
    """Class for implementing the player object."""

    def __init__(self, img: str):
        """Initialize player object."""
        GameObject.__init__(self, img)
        self.last_position = self.rect.center
        print(f"CENTER {self.last_position}")
        obstacles = {}
    
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
        # TODO: Dont move through other objects
        print(other.rect.left, other.rect.top, other.rect.right, other.rect.bottom)
        print(self.rect.left, self.rect.top, self.rect.right, self.rect.bottom)
        # TODO: Figure this out?
        toleft = other.rect.left < self.rect.left
        below = other.rect.bottom > self.rect.bottom
        toright = other.rect.right > self.rect.right
        above = other.rect.top < self.rect.top
        print(f"left? {toleft} right? {toright} above? {above} below? {below}")

        overlaps = (
            self.rect.left - other.rect.right,
            self.rect.top - other.rect.bottom,
            other.rect.left - self.rect.left,
            other.rect.top - self.rect.bottom,
        )
        print(overlaps)
        pass

    def on_collision_exit(self, other: GameObject) -> None:
        """Handle collision exit."""
        pass
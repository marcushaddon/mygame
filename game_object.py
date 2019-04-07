"""Code relating to game objects."""
import pygame


class GameObject(object):
    """Define behavior for game objects."""

    _id = 0

    def __init__(self, img: str):
        """Initialize game object."""
        self._id = GameObject._id
        GameObject._id = GameObject._id + 1
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.collisions = []
    
    def next(self) -> None:
        """Process tick of event loop."""
        pass
    
    def on_collision_enter(self, other) -> None:
        """Handle collision enter."""
        pass
    
    def on_collision_exit(self, other) -> None:
        """Handle collision exit."""
        pass
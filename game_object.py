"""Code relating to game objects."""
import pygame


class GameObject(object):
    """Define behavior for game objects."""

    def __init__(self, img: str):
        """Initialize game object."""
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.collisions = []
    
    def next(self) -> None:
        """Process tick of event loop."""
        pass
    
    def on_collision_enter(self, obj) -> None:
        """Handle collision enter."""
        print(f"I'm colliding {self}")
        pass
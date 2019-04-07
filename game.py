"""Code for managing game state."""
from typing import Tuple

import pygame

from game_object import GameObject

class Game(object):
    """Class for managing game objects."""

    def __init__(self, screen):
        """Instantiate game."""
        self.screen = screen
        self.game_objects = {}
        self.bg_color = 255, 255, 255
        self.active_collisions = {}
    
    def spawn(self, obj: GameObject, xy = None) -> int:
        """Spawn a game object."""
        self.game_objects[obj._id] = obj
        if xy is not None:
            obj.rect = obj.img.get_rect(
                center = xy
            )
        self.screen.blit(obj.img, obj.rect)
    
    def draw(self):
        """Process tick of event loop."""
        self._detect_collisions()
        self.screen.fill(self.bg_color)

        for _, obj in self.game_objects.items():
            obj.next()
            self.screen.blit(obj.img, obj.rect)

        pygame.display.flip()
        pygame.event.pump()
    
    def _detect_collisions(self) -> None:
        """Detect collisions between game objects."""
        # TODO: Make this not naiive!
        objs = [o for _, o in self.game_objects.items()]
        for i, a in enumerate(objs):
            for b in objs[i+1:]:
                colliding = pygame.sprite.collide_rect(a, b)
                collision_id = f"{a._id}|{b._id}"
                known_collision = collision_id in self.active_collisions

                # Possibly trigger collision
                if colliding:
                    if known_collision:
                        continue
                    self.active_collisions[collision_id] = True
                    a.on_collision_enter(b)
                    b.on_collision_enter(a)
                # Possibly record collision end
                else:
                    if known_collision:
                        a.on_collision_exit(b)
                        b.on_collision_exit(a)
                        del self.active_collisions[collision_id]
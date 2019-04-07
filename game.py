"""Code for managing game state."""

import pygame

class Game(object):
    """Class for managing game objects."""

    def __init__(self, screen):
        """Instantiate game."""
        self.screen = screen
        self.game_objects = {}
        self.game_objects_list = []
        self.bg_color = 255, 255, 255
        self.object_count = 0
    
    def spawn(self, obj, xy = (0, 0)) -> int:
        """Spawn a game object."""
        self.game_objects_list.append(obj)
        self.game_objects[self.object_count] = obj
        self.object_count += 1
        self.screen.blit(obj.img, obj.rect)
    
    def draw(self):
        """Process tick of event loop."""
        self.screen.fill(self.bg_color)

        for obj in self.game_objects_list:
            self._detect_collisions()
            obj.next()
            self.screen.blit(obj.img, obj.rect)

        pygame.display.flip()
        pygame.event.pump()
    
    def _detect_collisions(self) -> None:
        """Detect collisions between game objects."""
        # TODO: Make this not naiive!
        for i, a in enumerate(self.game_objects_list):
            for b in self.game_objects_list[i+1:]:
                if pygame.sprite.collide_rect(a, b):
                    print(f"COLLISION {a} {b}")

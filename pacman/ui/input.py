import pygame


class InputManager:
    """Manage player keyboard input."""

    def get_direction(
        self,
        event: pygame.event.Event
    ) -> str | None:

        """Return the requested movement direction."""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                return "UP"
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                return "DOWN"
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                return "LEFT"
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                return "RIGHT"
        return None
                
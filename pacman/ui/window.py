import pygame


class Window:
    """Manage the graphical window of Pac-Man."""

    def __init__(self, width: int, height: int,
                 title: str) -> None:
        """Initialize Pygame and create the window."""
        self.width = width
        self.height = height
        self.title = title

        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption(self.title)

    def clear(self, color: tuple[int, int, int]) -> None:
        """Fill the display surface with the given color."""
        self.screen.fill(color)

    def refresh(self) -> None:
        """Update the display with the current frame."""
        pygame.display.flip()

    def close(self) -> None:
        """Release Pygame resources."""
        pygame.quit()

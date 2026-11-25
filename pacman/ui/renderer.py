from pacman.ui.constants import CELL_SIZE, YELLOW
import pygame


class Renderer:
    """Render the graphical elements of Pac-Man."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize the renderer."""
        self.screen = screen

    def draw_player(self, row: int, col: int) -> None:
        """Draw Pac-Man at the given maze position."""

        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        radius = CELL_SIZE // 2 - 3

        pygame.draw.circle(
            self.screen,
            YELLOW,
            (x, y),
            radius
        )

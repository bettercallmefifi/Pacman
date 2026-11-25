from pacman.ui.window import Window
import pygame
from pacman.ui.constants import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    WINDOW_TITLE,
    FPS,
    BLACK,
    CELL_SIZE
)
from pacman.ui.input import InputManager
from pacman.ui.renderer import Renderer


class App:
    """Manage the Pac-Man application."""

    def __init__(self) -> None:
        """Initialize the application."""
        self.window = Window(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
            WINDOW_TITLE,
        )
        self.running = True
        self.clock = pygame.time.Clock()
        self.input_manager = InputManager()
        self.renderer = Renderer(self.window.screen)
        self.player_row = 2
        self.player_col = 3

    def handle_events(self) -> None:
        for event in pygame.event.get():
            direction = self.input_manager.get_direction(
                event
            )
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stop()
            if direction == "UP":
                if self.player_row > 0:
                    self.player_row -= 1
            elif direction == "DOWN":
                if self.player_row < WINDOW_HEIGHT // CELL_SIZE - 1:
                    self.player_row += 1
            elif direction == "LEFT":
                if self.player_col > 0:
                    self.player_col -= 1
            elif direction == "RIGHT":
                if self.player_col < WINDOW_WIDTH // CELL_SIZE - 1:
                    self.player_col += 1
                

    def run(self) -> None:
        """Execute the main application loop."""
        try:
            while self.running:
                self.handle_events()

                if not self.running:
                    break

                self.window.clear(BLACK)
                self.renderer.draw_player(
                    self.player_row,
                    self.player_col
                )
                self.window.refresh()
                self.clock.tick(FPS)
        finally:    
            self.window.close()

    def stop(self) -> None:
        """Stop the application loop."""
        self.running = False


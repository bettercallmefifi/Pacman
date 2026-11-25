from pacman.ui.window import Window
import pygame
from pacman.ui.constants import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    WINDOW_TITLE,
    FPS,
    BLACK,
)
from pacman.ui.input import InputManager


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
            if direction is not None:
                print(direction)
                

    def run(self) -> None:
        """Execute the main application loop."""
        try:
            while self.running:
                self.handle_events()

                if not self.running:
                    break

                self.window.clear(BLACK)
                self.window.refresh()
                self.clock.tick(FPS)
        finally:    
            self.window.close()

    def stop(self) -> None:
        """Stop the application loop."""
        self.running = False


from pacman.ui.window import Window
import pygame
from pacman.ui.constants import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    WINDOW_TITLE,
    FPS,
    BLACK,
    CELL_SIZE,
    RED,
    PINK,
    CYAN,
    ORANGE,
)
from pacman.ui.input import InputManager
from pacman.ui.renderer import Renderer
# from pacman.mazegenerator import MazeGenerator


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
        self.player_row = 0
        self.player_col = 0
        # self.mazee = MazeGenerator()
        # self.mazee.generate()
        # self.mazze = self.mazee.maze
        # print(self.mazze)
        self.maze =  [
            [["N", "S", "W"], ["N", "S"], ["N", "E"]],
            [["N", "S", "W"], ["N", "S"], ["S", "E"]]
        ]
        self.pacgums = [
            (0, 1),
            (0, 2),
            (1, 1)
        ]

        self.super_pacgums = [
            (1, 0),
            (1, 2)
        ]

        self.ghosts = [
            (0, 2, RED, False),
            (1, 0, PINK, False),
            (1, 1, CYAN, False),
            (1, 2, ORANGE, True)
        ]

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
                self.renderer.draw_maze(self.maze) 
                for row, col in self.pacgums:
                    self.renderer.draw_pacgum(row, col)

                for row, col in self.super_pacgums:
                    self.renderer.draw_super_pacgum(row, col)               

                for row, col, color, edible in self.ghosts:
                    self.renderer.draw_ghost(
                        row,
                        col,
                        color,
                        edible
                    )

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


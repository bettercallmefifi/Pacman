from pacman.ui.constants import (
    CELL_SIZE,
    YELLOW,
    BLUE,
    WHITE,
    WALL_THICKNESS,
    PACGUM_RADIUS,
    SUPER_PACGUM_RADIUS,
    DARK_BLUE,
)
import pygame


class Renderer:
    """Render the graphical elements of Pac-Man."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize the renderer."""
        self.screen = screen

    def draw_player(self, row: int, col: int) -> None:
        """Draw Pac-Man at the given maze position."""

        x, y = self.cell_center(row, col)
        radius = CELL_SIZE // 2 - 3

        pygame.draw.circle(
            self.screen,
            YELLOW,
            (x, y),
            radius
        )

    def draw_wall(
        self,
        row: int,
        col: int,
        side: str
    ) -> None:
        """Draw a wall on the specified side of a cell."""
        x = col * CELL_SIZE
        y = row * CELL_SIZE

        if side == "N":
            pygame.draw.rect(
                self.screen,
                BLUE,
                (
                    x,
                    y,
                    CELL_SIZE,
                    WALL_THICKNESS
                )
            )
        elif side == "S":
            pygame.draw.rect(
                self.screen,
                BLUE,
                (
                    x,
                    y + CELL_SIZE - WALL_THICKNESS,
                    CELL_SIZE,
                    WALL_THICKNESS
                )
            )
        elif side == "E":
            pygame.draw.rect(
                self.screen,
                BLUE,
                (
                    x + CELL_SIZE - WALL_THICKNESS,
                    y,
                    WALL_THICKNESS,
                    CELL_SIZE
                )
            )
        elif side == "W":
            pygame.draw.rect(
                self.screen,
                BLUE,
                (
                    x,
                    y,
                    WALL_THICKNESS,
                    CELL_SIZE
                )
            )

    def draw_maze(
        self,
        maze: list[list[list[str]]]
    ) -> None:
        """Draw all the walls of the maze."""
        for row, cells in enumerate(maze):
            for col, walls in enumerate(cells):
                for side in walls:
                    self.draw_wall(row, col, side)

    def cell_center(
        self,
        row: int,
        col: int
    ) -> tuple[int, int]:
        """Return the pixel coordinates of a cell center."""
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        return x, y

    def draw_pacgum(self, row: int, col: int) -> None:
        """Draw a normal pacgum."""
        x, y = self.cell_center(row, col)
        pygame.draw.circle(
            self.screen,
            WHITE,
            (x, y),
            PACGUM_RADIUS
        )

    def draw_super_pacgum(self, row: int, col: int) -> None:
        """Draw a super pacgum."""
        x, y = self.cell_center(row, col)
        pygame.draw.circle(
            self.screen,
            WHITE,
            (x, y),
            SUPER_PACGUM_RADIUS
        )

    def draw_ghost(
        self,
        row: int,
        col: int,
        color: tuple[int, int, int],
        edible: bool
    ) -> None:
        """Draw a ghost according to its current state."""
        x, y = self.cell_center(row, col)
        radius = CELL_SIZE // 2 - 3

        if edible:
            body_color = DARK_BLUE
        else:
            body_color = color

        pygame.draw.circle(
            self.screen,
            body_color,
            (x, y),
            radius
        )
        pygame.draw.rect(
            self.screen,
            body_color,
            (
                x - radius,
                y,
                radius * 2,
                radius
            )
        )
        pygame.draw.circle(
            self.screen,
            WHITE,
            (
                x - 4,
                y - 3
            ),
            3
        )
        pygame.draw.circle(
            self.screen,
            WHITE,
            (
                x + 4,
                y - 3
            ),
            3
        )
        pygame.draw.circle(
            self.screen,
            BLUE,
            (
                x - 4,
                y - 3
            ),
            1
        )
        pygame.draw.circle(
            self.screen,
            BLUE,
            (
                x + 4,
                y - 3
            ),
            1
        )
        
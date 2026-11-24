import pygame
from pacman.ui.window import Window


def main() -> None:
    """Test the Window class."""
    window = Window(900, 700, "Pac-Man")
    running = True
    clock = pygame.time.Clock()

    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            window.clear((255, 255, 0))
            window.refresh()
            clock.tick(60)
    finally:
        window.close()


if __name__ == "__main__":
    main()
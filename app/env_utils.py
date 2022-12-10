from pathlib import Path

import pygame

IMAGES_FOLDER = Path(__file__).parent / "images"


def get_screen(width: int, height: int):
    screen = pygame.display.set_mode((width, height))
    icon = pygame.image.load(IMAGES_FOLDER / "logo.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("AoT: Split Attention")
    return screen

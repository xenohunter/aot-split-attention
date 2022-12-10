import pygame

from .element import Element


class Button(Element):

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def is_clicked(self, x, y):
        return self.rect.collidepoint(x, y)

    def render(self, screen):
        pygame.draw.rect(screen, [255, 255, 255], self.rect)

from app.elements import Button

from .stage import Stage


class Menu(Stage):

    def __init__(self):
        self.button = Button(0, 0, 100, 100)

    def handle(self, event):
        pass

    def update(self, _, app):
        pass

    def render(self, screen):
        self.button.render(screen)

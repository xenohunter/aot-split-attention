from .stage import Stage
from .menu import Menu
from .overlay import Overlay


class Opening(Stage):

    def __init__(self):
        self.freq = 5
        self.counter = 500 * 5

    def update(self, _, app):
        self.counter -= 1
        if self.counter == 0:
            app.register_overlay(Overlay())
            app.register(Menu())

    def render(self, screen):
        x = max(0, min(255, self.counter // self.freq))
        screen.fill([x, x, x])

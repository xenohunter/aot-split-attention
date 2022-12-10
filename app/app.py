import pygame

from .env_utils import get_screen
from .global_state import GlobalState
from .stages import Opening, Stage


class App:

    def __init__(self):
        self.width = 640
        self.height = 400

        self.screen = None
        self.global_state: GlobalState = None

        self.current_overlay: Stage = None
        self.next_overlay: Stage = None
        self.current_stage: Stage = None
        self.next_stage: Stage = None

        self.is_running = False

    def handle(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
        else:
            if self.current_overlay:
                self.current_overlay.handle(event)
            self.current_stage.handle(event)

    def update(self):
        if self.current_overlay:
            self.current_overlay.update(self.global_state, self)
        self.current_stage.update(self.global_state, self)

    def render(self):
        self.current_stage.render(self.screen)
        if self.current_overlay:
            self.current_overlay.render(self.screen)
        pygame.display.update()

    def register(self, stage):
        self.next_stage = stage

    def register_overlay(self, overlay):
        self.next_overlay = overlay

    def unregister_overlay(self):
        self.current_overlay = None
        self.next_overlay = None

    def resolve(self):
        if self.next_overlay:
            self.current_overlay = self.next_overlay
            self.next_overlay = None
        if self.next_stage:
            self.current_stage = self.next_stage
            self.next_stage = None

    def start(self):
        pygame.init()

        self.screen = get_screen(self.width, self.height)
        self.global_state = GlobalState()
        self.current_stage = Opening()
        self.is_running = True

        while self.is_running:
            for event in pygame.event.get():
                self.handle(event)
            self.update()
            self.render()
            self.resolve()

        pygame.quit()

class GlobalState:

    def __init__(self):
        self.user = None
        self.fg_score = 0
        self.bg_score = 0

    def set_user(self, name: str):
        self.user = name

    def add_fg_score(self, addition):
        self.fg_score += addition

    def add_bg_score(self, addition):
        self.bg_score += addition

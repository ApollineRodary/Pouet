from ui.scene import Scene
from objects.button import Button
from .level_selector import LevelSelector

class Menu(Scene):
    def __init__(self):
        self.start_button = Button(
            x = 600, y = 300,
            width = 500, height = 100,
            text = "Start game",
        )

        self.quit_button = Button(
            x = 600, y = 500,
            width = 500, height = 100,
            text = "Quit game"
        )
        self.quit_button.set_command(lambda _: exit())

        super().__init__([
            self.start_button,
            self.quit_button
        ])

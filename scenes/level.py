from ui.scene import Scene
from objects.button import Button

class Level(Scene):
    def __init__(self, name: str):
        self.play_button = Button(
            x = 1050, y = 650,
            width = 200, height = 200,
            text = "Play"
        )
        self.home_button = Button(
            x=800, y = 650,
            width = 200, height = 200,
            text = "Back"
        )

        super().__init__([
            self.play_button,
            self.home_button
        ])

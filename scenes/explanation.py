from ui.scene import Scene
from objects.button import Button
from scenes.level import Level
from objects.text import Text

class Explanation(Scene):
    def __init__(self, expl: str, next_level: Level):
        self.next_button = Button(
            x = 1050, y = 650,
            width = 200, height = 200,
            text = "Next"
        )
        self.expl = Text(
            text = expl
        )

        super().__init__([
            self.next_button,
            self.expl
        ])

        self.next_button.set_command(lambda _: self.next_button.canvas.load(next_level))
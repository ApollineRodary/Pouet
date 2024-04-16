from ui.scene import Scene
from objects.button import Button
from scenes.level import Level
from objects.text import Text
from objects.picture import Picture


class Explanation(Scene):
    def __init__(self, expl: str, picture: str, next_level: Level):
        self.next_button = Button(
            x = 1050, y = 650,
            width = 200, height = 200,
            text = "Next"
        )
        self.expl = Text(
            text = expl
        )

        if picture != '':
            self.image = Picture(
                picture = picture
            )
            init = [
            self.next_button,
            self.expl,
            self.image
            ]

        else:
            init = [
            self.next_button,
            self.expl
            ]

        super().__init__(init)

        self.next_button.set_command(lambda _: self.next_button.canvas.load(next_level))
from ui.scene import Scene
from objects.button import Button
from objects.text import Text
from objects.picture import Picture


class Victory(Scene):
    def __init__(self):
        self.next_button = Button(
            x = 1050, y = 650,
            width = 200, height = 200,
            text = "Next"
        )
        self.expl = Text(
            text = "Congratulations !"
        )

        self.image = Picture(
            picture = "assets/images/victory.png",
            size = (200, 200)
        )


        super().__init__([
            self.next_button,
            self.expl,
            self.image
        ])

        self.next_button.set_command(
            lambda _: self.next_button.canvas.load(self.next)
        )

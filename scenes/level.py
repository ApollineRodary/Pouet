from ui.scene import Scene
from objects.button import Button
from objects.comparator import Comparator
from objects.source_array import SourceArray

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
        self.source_array = SourceArray(80, 100, 6)
        self.comparators = [
            Comparator(100 + i*10, 400 + i*10) for i in range(13)
        ]
        self.play_button.set_command(
            lambda _: self.source_array.activate(self.comparators)
        )

        super().__init__(
            self.comparators + [
                self.play_button,
                self.home_button,
                self.source_array
            ]
        )

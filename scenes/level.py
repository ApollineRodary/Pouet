from ui.scene import Scene
from objects.button import Button
from objects.block import Block
from objects.source_array import SourceArray
from objects.target_array import TargetArray

class Level(Scene):
    def __init__(self, name: str, array_size: int, blocks: list[Block]):
        self.name = name

        play_button = Button(
            x = 1050, y = 650,
            width = 200, height = 200,
            text = "Play"
        )
        self.home_button = Button(
            x=800, y = 650,
            width = 200, height = 200,
            text = "Back"
        )
        source_array = SourceArray(80, 100, array_size)
        target_array = TargetArray(1120, 100, array_size)

        play_button.set_command(
            lambda _: source_array.activate(
                blocks=blocks,
                target=target_array
            )
        )

        super().__init__(
            blocks + [
                play_button,
                self.home_button,
                source_array,
                target_array
            ]
        )

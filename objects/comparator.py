from .block import Block
import tkinter

COMPARATOR_IMAGE = tkinter.PhotoImage(file = "assets/textures/comparator.png")

class Comparator(Block):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, size=2)

    def on_traversed(self, inputs):
        super().on_traversed(inputs)
        return [1, 0] if inputs[0] > inputs[1] else [0, 1]

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)
        self.image = canvas.create_image(
            self.x,
            self.y,
            image = COMPARATOR_IMAGE
        )

    def unload(self):
        self.canvas.delete(self.image)
        super().unload()

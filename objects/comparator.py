from .block import Block
import tkinter

SPRITES = {
    "idle": tkinter.PhotoImage(file="assets/textures/comparator_idle.png"),
    "hovered": tkinter.PhotoImage(file="assets/textures/comparator_hovered.png"),
    "held": tkinter.PhotoImage(file="assets/textures/comparator_held.png"),
    "clicked": tkinter.PhotoImage(file="assets/textures/comparator_clicked.png")
}

class Comparator(Block):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, size=2, sprites=SPRITES)

    def on_traversed(self, inputs):
        super().on_traversed(inputs)
        return [1, 0] if inputs[0] > inputs[1] else [0, 1]

    def unload(self):
        self.canvas.delete(self.image)
        super().unload()

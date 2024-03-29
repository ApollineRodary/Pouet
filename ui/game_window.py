import tkinter
from .game_canvas import GameCanvas

TITLE = "Pouet :)"

class GameWindow(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(TITLE)

        self.canvas = GameCanvas(self)
        self.canvas.grid()


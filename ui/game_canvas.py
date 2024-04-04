import tkinter
from .scene import Scene

CANVAS_BACKGROUND_COLOR = "#ffe0e0"
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800

class GameCanvas(tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.config(background=CANVAS_BACKGROUND_COLOR)
        self.scene = None

    def load(self, scene: Scene):
        if self.scene:
            self.scene.unload()
        self.scene = scene
        self.scene.load(self)
        self.update()

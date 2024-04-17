from .object import Object
import tkinter
import pyglet

TEXT_COLOR = "black"

class Text(Object):
    def __init__(self,text: str, x=600, y=200):
        self.text = text
        super().__init__(x, y)

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)

        self.expl = self.canvas.create_text(
            self.x, self.y,
            text = self.text,
            fill = TEXT_COLOR,
            font = ('CatComic', '30', 'bold'),
            width = 900
        )


    def unload(self):
        self.canvas.delete(self.expl)
        super().unload()
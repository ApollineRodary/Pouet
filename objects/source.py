from .object import Object
import tkinter

SOURCE_RADIUS = 5
SOURCE_WIDTH = 2
SOURCE_OUTLINE_COLOR = "purple"

class Source(Object):
    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)

        self.circle = self.canvas.create_oval(
            self.x - SOURCE_RADIUS,
            self.y - SOURCE_RADIUS,
            self.x + SOURCE_RADIUS,
            self.y + SOURCE_RADIUS,
            outline = SOURCE_OUTLINE_COLOR,
            width = SOURCE_WIDTH
        )

    def unload(self):
        self.canvas.delete(self.circle)
        super().unload()

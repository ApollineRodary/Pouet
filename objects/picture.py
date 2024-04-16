from .object import Object
import tkinter

class Picture(Object):
    def __init__(self, picture: str, x=600, y=600):
        super().__init__(x, y)
        self.picture = tkinter.PhotoImage(file = picture)

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)

        self.image = canvas.create_image(
            self.x,
            self.y,
            image = self.picture
        )


    def unload(self):
        self.canvas.delete(self.image)
        super().unload()
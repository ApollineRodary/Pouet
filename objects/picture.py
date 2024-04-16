from .object import Object
import tkinter
from PIL import Image, ImageTk

class Picture(Object):
    def __init__(self, picture: str, size, x=600, y=600):
        super().__init__(x, y)
        image = Image.open(picture)
        img = image.resize(size)
        self.picture = ImageTk.PhotoImage(img)

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
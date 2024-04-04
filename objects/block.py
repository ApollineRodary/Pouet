from .object import Object
import tkinter
from playsound import playsound

class Block(Object):
    def __init__(self, x: int, y: int, size: int):
        super().__init__(x, y)
        self.size = size

    def on_traversed(self, inputs):
        assert len(inputs) == self.size

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)
        self.image = canvas.create_image(
            self.x,
            self.y
        )
        self.canvas.tag_bind(self.image, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.image, "<ButtonRelease-1>", self.on_drop)
        self.canvas.tag_bind(self.image, "<ButtonPress-1>", self.on_start)

    def on_drag(self, event):
        xd = event.x
        yd = event.y
        if not (xd<0 or xd>1200 or yd<0 or yd>800):
            self.canvas.coords(self.image, [xd, yd])

    def on_drop(self, event):
        playsound('assets/sounds/drop_block.wav', block=False)
    
    def on_start(self, event):
        playsound('assets/sounds/drag_block.mp3', block=False)

    def set_command(self, f: callable):
        self.command = f
        self.update()

    def on_hover(self, event):
        self.canvas.itemconfig(
            self.rectangle,
            outline = BUTTON_OUTLINE_HOVER_COLOR
        )
        self.canvas.itemconfig(
            self.label,
            fill = BUTTON_LABEL_HOVER_COLOR
        )

    def on_leave(self, event):
        self.canvas.itemconfig(
            self.rectangle,
            outline = BUTTON_OUTLINE_COLOR
        )
        self.canvas.itemconfig(
            self.label,
            fill = BUTTON_LABEL_COLOR
        )


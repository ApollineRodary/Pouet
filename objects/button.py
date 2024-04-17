from .object import Object
import tkinter
from playsound import playsound

BUTTON_LABEL_COLOR = "#ffaa00"
BUTTON_LABEL_HOVER_COLOR = "#ff8000"

SPRITE_BUTTON = tkinter.PhotoImage(file="assets/textures/button.png")

class Button(Object):
    def __init__(
        self, x=0, y=0, width=0, height=0,
        text="", command = lambda _: None
    ):
        super().__init__(x, y)
        self.width, self.height = width, height
        self.text = text
        self.command = command

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)

        self.image = self.canvas.create_image(
            self.x, self.y,
            image = SPRITE_BUTTON
        )

        self.label = self.canvas.create_text(
            self.x, self.y,
            text = self.text,
            fill = BUTTON_LABEL_COLOR,
            font = ('CatComic', '20', 'bold'),
            width = self.width
        )

        self.tag = f"button_{self.image}_{self.label}"
        self.canvas.addtag(self.tag, 'withtag', self.image)
        self.canvas.addtag(self.tag, 'withtag', self.label)

        self.canvas.tag_bind(
            self.tag, "<Button-1>",
            lambda _: playsound("assets/sounds/button.wav", block=False)
        )
        self.canvas.tag_bind(self.tag, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.tag, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.tag, "<Button-1>", self.command, add=True)

    def unload(self):
        self.canvas.delete(self.tag)
        super().unload()

    def set_command(self, f: callable):
        self.command = f
        if self.visible:
            self.canvas.tag_bind(self.tag, "<Button-1>", self.command, add=True)

    def on_hover(self, event):
        self.canvas.itemconfig(
            self.label,
            fill = BUTTON_LABEL_HOVER_COLOR
        )

    def on_leave(self, event):
        self.canvas.itemconfig(
            self.label,
            fill = BUTTON_LABEL_COLOR
        )

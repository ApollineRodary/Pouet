from .object import Object
import tkinter

BUTTON_OUTLINE_COLOR = "white"
BUTTON_FILL_COLOR = "#0c0c0c"
BUTTON_LABEL_COLOR = "white"
BUTTON_OUTLINE_HOVER_COLOR = "yellow"
BUTTON_LABEL_HOVER_COLOR = "yellow"

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

        self.min_x = self.x - self.width/2
        self.min_y = self.y - self.height/2
        self.max_x = self.x + self.width/2
        self.max_y = self.y + self.height/2

        self.rectangle = self.canvas.create_rectangle(
            self.min_x, self.min_y, self.max_x, self.max_y,
            outline = BUTTON_OUTLINE_COLOR,
            fill = BUTTON_FILL_COLOR,
            width = 3
        )

        self.label = self.canvas.create_text(
            self.x, self.y,
            text = self.text,
            fill = BUTTON_LABEL_COLOR
        )

        self.canvas.tag_bind(self.rectangle, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.rectangle, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.command)

    def unload(self):
        self.canvas.delete(self.rectangle)
        self.canvas.delete(self.label)
        super().unload()

    def set_command(self, f: callable):
        self.command = f
        if self.visible:
            self.canvas.tag_bind(self.rectangle, "<Button-1>", self.command)

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

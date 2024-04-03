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
        self.rectangle = self.canvas.create_rectangle(0, 0, 0, 0)
        self.label = self.canvas.create_text(0, 0)
        self.update()

    def unload(self):
        self.canvas.delete(self.rectangle)
        self.canvas.delete(self.label)
        super().unload()

    def update(self):
        super().update()

        # Update bounding box
        self.min_x = self.x - self.width/2
        self.min_y = self.y - self.height/2
        self.max_x = self.x + self.width/2
        self.max_y = self.y + self.height/2

        # Stop here if the button is not on the current scene
        if not self.visible:
            return

        # Move and configure rectangle
        self.canvas.coords(
            self.rectangle, [
                self.min_x,
                self.min_y,
                self.max_x,
                self.max_y
            ]
        )
        self.canvas.itemconfig(
            self.rectangle,
            outline = BUTTON_OUTLINE_COLOR,
            fill = BUTTON_FILL_COLOR,
            width = 3
        )

        # Move and configure label
        self.canvas.coords(
            self.label, [
                self.x,
                self.y
            ]
        )
        self.canvas.itemconfig(
            self.label,
            text = self.text,
            fill = BUTTON_LABEL_COLOR
        )

        # Handle color change when the button is hovered
        self.canvas.tag_bind(self.rectangle, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.rectangle, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.command)

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

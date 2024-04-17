from .object import Object
import tkinter
import pygame.mixer

DROP_BLOCK_SOUND = pygame.mixer.Sound("assets/sounds/drop_block.wav")
DRAG_BLOCK_SOUND = pygame.mixer.Sound("assets/sounds/drag_block.mp3")

class Block(Object):
    def __init__(self, x: int, y: int, size: int, sprites: dict):
        super().__init__(x, y)
        self.size = size
        self.sprites = sprites

    def on_traversed(self, inputs):
        assert len(inputs) == self.size

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)
        self.image = canvas.create_image(
            self.x,
            self.y,
            image = self.sprites["idle"]
        )
        self.canvas.tag_bind(self.image, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.image, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.image, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.image, "<ButtonRelease-1>", self.on_drop)
        self.canvas.tag_bind(self.image, "<ButtonPress-1>", self.on_start)

    def on_hover(self, event):
        self.canvas.itemconfig(self.image, image=self.sprites["hovered"])

    def on_leave(self, event):
        self.canvas.itemconfig(self.image, image=self.sprites["idle"])

    def on_drag(self, event):
        xd = event.x
        yd = event.y
        if (0<xd<1200 and 0<yd<800):
            self.canvas.coords(self.image, [xd, yd])

    def on_drop(self, event):
        DROP_BLOCK_SOUND.play()
        self.canvas.itemconfig(self.image, image=self.sprites["hovered"])

    def on_start(self, event):
        DRAG_BLOCK_SOUND.play()
        self.canvas.itemconfig(self.image, image=self.sprites["clicked"])
        self.canvas.after(
            100,
            lambda: self.canvas.itemconfig(
                self.image,
                image=self.sprites["held"]
            )
        )

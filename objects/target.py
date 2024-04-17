from .object import Object
import tkinter
import pygame.mixer

TARGET_RADIUS = 5
TARGET_WIDTH = 2
TARGET_OUTLINE_COLOR = "orange"

SPRITE_WRONG = tkinter.PhotoImage(file="assets/textures/wrong_value.png")
SPRITE_CORRECT = tkinter.PhotoImage(file="assets/textures/correct_value.png")

DEFEAT_SOUND = pygame.mixer.Sound("assets/sounds/defeat.mp3")
VICTORY_SOUND = pygame.mixer.Sound("assets/sounds/victory.mp3")

class Target(Object):
    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)

        self.image = None
        self.circle = self.canvas.create_oval(
            self.x - TARGET_RADIUS,
            self.y - TARGET_RADIUS,
            self.x + TARGET_RADIUS,
            self.y + TARGET_RADIUS,
            outline = TARGET_OUTLINE_COLOR,
            width = TARGET_WIDTH
        )

    def unload(self):
        self.canvas.delete(self.circle)
        if self.image != None:
            self.canvas.delete(self.image)
        super().unload()

    def set_wrong(self):
        DEFEAT_SOUND.play()
        if self.image:
            self.canvas.delete(self.image)
        self.image = self.canvas.create_image(
            self.x, self.y,
            image = SPRITE_WRONG
        )

    def set_correct(self):
        VICTORY_SOUND.play()
        if self.image:
            self.canvas.delete(self.image)
        self.image = self.canvas.create_image(
            self.x, self.y,
            image = SPRITE_CORRECT
        )


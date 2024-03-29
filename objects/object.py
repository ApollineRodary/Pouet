import tkinter

class Object:
    """Any object on the game canvas"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.visible = False

    def load(self, canvas: tkinter.Canvas):
        self.canvas = canvas
        self.visible = True

    def unload(self):
        self.canvas = None
        self.visible = False

    def update(self):
        pass

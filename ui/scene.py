import tkinter

class Scene:
    def __init__(self, objects: list):
        self.objects = objects

    def add_object(self, object: any):
        self.objects.append(object)

    def load(self, canvas: tkinter.Canvas):
        for object in self.objects:
            object.load(canvas)

    def unload(self):
        for object in self.objects:
            object.unload()

    def add_next(self, next):
        self.next = next

from .object import Object

class Block(Object):
    def __init__(self, x: int, y: int, size: int):
        super().__init__(x, y)
        self.size = size

    def on_traversed(self, inputs):
        assert len(inputs) == self.size

from .object import Object
from .target import Target
from .light_beam import LightBeam
import tkinter

TARGET_DISTANCE = 60
TICK_TIME = 20

class TargetArray(Object):
    def __init__(self, x: int, y: int, targets: int):
        super().__init__(x, y)

        self.targets = []
        for i in range(targets):
            self.targets.append(Target(x, y + i*TARGET_DISTANCE))

        self.active = False

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)
        for target in self.targets:
            target.load(canvas)

    def unload(self):
        if self.active:
            self.deactivate()
        for target in self.targets:
            target.unload()
        super().unload()

    def verify(self, beams: list[LightBeam]):
        values = sorted([beam.value for beam in beams])

        for i, target in enumerate(self.targets):
            x1, y1, x2, y2 = self.canvas.bbox(target.circle)
            input_beams = list(filter(
                lambda beam: (
                    x1 < beam.current_x < x2
                    and y1 < beam.current_y < y2
                ),
                beams
            ))

            assert(len(input_beams) == 1)
            beam = input_beams[0]
            if beam.value != values[i]:
                self.canvas.after(i*200, target.set_wrong)
            else:
                self.canvas.after(i*200, target.set_correct)


from .object import Object
from .source import Source
from .block import Block
from .light_beam import LightBeam
from .target_array import TargetArray
import tkinter

SOURCE_DISTANCE = 60
TICK_TIME = 20

class SourceArray(Object):
    def __init__(self, x: int, y: int, sources: int):
        super().__init__(x, y)

        self.sources = []
        self.beams = []
        for i in range(sources):
            self.sources.append(Source(x, y + i*SOURCE_DISTANCE))

        self.active = False

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)
        for source in self.sources:
            source.load(canvas)

    def unload(self):
        if self.active:
            self.deactivate()
        for source in self.sources:
            source.unload()
        super().unload()

    def activate(self, blocks: list[Block], target: TargetArray):
        if self.active:
            self.deactivate()

        self.blocks = blocks
        self.target = target
        for value, source in enumerate(self.sources):
            beam = LightBeam(source.x, source.y, 5-value)
            beam.load(self.canvas)
            self.beams.append(beam)

        self.active = True
        self.tick()

    def tick(self):
        if not self.active:
            return
        for beam in self.beams:
            beam.tick()

        for block in self.blocks:
            x1, y1, x2, y2 = self.canvas.bbox(block.image)
            input_beams = list(filter(
                lambda beam: (
                    x1 < beam.current_x < x2
                    and y1 < beam.current_y < y2
                    and not block in beam.blocks_to_ignore
                ),
                self.beams
            ))
            input_beams.sort(key = lambda beam: beam.current_y)
            input_values = [beam.value for beam in input_beams]

            if len(input_beams) != block.size:
                continue

            permutation = block.on_traversed(input_values)
            for i, beam in enumerate(input_beams):
                beam.offset(SOURCE_DISTANCE * (permutation[i] - i), 100)
                beam.blocks_to_ignore.append(block)

        beam_position = self.beams[0].current_x
        if beam_position < self.target.x:
            self.loop_task_id = self.canvas.after(TICK_TIME, self.tick)
        else:
            self.target.verify(self.beams)

    def deactivate(self):
        for beam in self.beams:
            beam.unload()
        self.blocks = []
        self.beams = []
        self.active = False
        self.canvas.after_cancel(self.loop_task_id)

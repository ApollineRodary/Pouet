from .object import Object
import tkinter
import colorsys

STEP_SIZE = 5
LINE_WIDTH = 4
OFFSET_SPEED = 4

def move_towards(origin: int, target: int, speed: int):
    if target > origin:
        return min(target, origin + speed)
    if target < origin:
        return max(target, origin - speed)
    return origin

def smootherstep(x):
    return 6*x**5 - 15*x**4 + 10*x**3

class LightBeam(Object):
    def __init__(self, x: int, y: int, value: int):
        super().__init__(x, y)
        self.value = value
        r, g, b = colorsys.hsv_to_rgb((value)/18, 1, 1)
        self.color = '#%02x%02x%02x' % (
            int(r * 255),
            int(g * 255),
            int(b * 255)
        )

        # Current segment, with beginning and end coordinates
        self.current_segment = None
        self.last_x, self.last_y = x, y
        self.current_x, self.current_y = x, y
        self.target_y = y

        # All segments, including those that are complete
        self.segments = []

        # Blocks that have already been traversed and should be ignored
        self.blocks_to_ignore = []

        self.offset_origin = None
        self.offset_target = None
        self.offset_length = 0
        self.offset_progress = 0

    def load(self, canvas: tkinter.Canvas):
        super().load(canvas)

    def unload(self):
        for segment in self.segments:
            self.canvas.delete(segment)
        super().unload()

    def tick(self):
        self.new_x = self.current_x + STEP_SIZE
        self.new_y = self.current_y
        if self.offset_length > 0:
            self.offset_progress = min(
                self.offset_progress + STEP_SIZE,
                self.offset_length
            )
            dy = smootherstep(self.offset_progress / self.offset_length) \
                * (self.offset_target - self.offset_origin)
            self.new_y = self.offset_origin + dy

        # If the beam should be bent upwards or downwards, create a new segment
        if self.new_y != self.last_y:
            self.last_x, self.last_y = self.current_x, self.current_y
            self.current_segment = None
        self.current_x, self.current_y = self.new_x, self.new_y

        if self.current_segment is None:
            self.current_segment = self.canvas.create_line(
                self.last_x,
                self.last_y,
                self.current_x,
                self.current_y,
                width = LINE_WIDTH,
                fill = self.color
            )
            self.segments.append(self.current_segment)
            return

        self.canvas.coords(
            self.current_segment,
            [self.last_x, self.last_y, self.current_x, self.current_y]
        )

    def offset(self, dy: int, length: int):
        self.offset_origin = self.current_y
        self.offset_progress = 0
        self.offset_length = length
        self.offset_target = self.current_y + dy

from scenes.level import Level
from objects.comparator import Comparator

start_level = Level(
    name = "Start",
    array_size = 2,
    blocks = [Comparator(500, 500)]
)

compare_three = Level(
    name = "Three-way",
    array_size = 3,
    blocks = [Comparator(600, 300), Comparator(700, 370)]
)

compare_four = Level(
    name = "Four-way",
    array_size = 4,
    blocks = [
        Comparator(400, 300), Comparator(530, 380),
        Comparator(600, 200), Comparator(380, 350),
        Comparator(610, 400)
    ]
)

levels = [
    start_level,
    compare_three,
    compare_four
]

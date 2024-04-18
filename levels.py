from scenes.level import Level
from objects.comparator import Comparator
from scenes.victory import Victory
from scenes.explanation import Explanation

start_level = Level(
    name = "Start",
    array_size = 2,
    blocks = [Comparator(500, 500)]
)

compare_three = Level(
    name = "Three-way",
    array_size = 3,
    blocks = [Comparator(600, 300), Comparator(700, 370),
              Comparator(600,200)]
)

compare_four = Level(
    name = "Four-way",
    array_size = 4,
    blocks = [
        Comparator(400, 300), Comparator(530, 380),
        Comparator(600, 200), Comparator(380, 350),
        Comparator(610, 400), Comparator(700,360)
    ]
)

compare_six = Level (
    name = "Six-way",
    array_size = 6,
    blocks = [
        Comparator(400+10*x,600+x) for x in range (15)
    ]
)

scenes = [
    Explanation("Hello! \n"
                "In this game, you will have to build a rainbow! For the first "
                "levels, sort the colours in the reverse order: the one on top "
                "has to go to the bottom and so on. To do so, use comparators like the one below."
                "It takes two colours, and puts them in the right order. \nGood luck!",
                'assets/textures/comparator_idle.png', (200, 200)),
    start_level,
    Explanation('Test', '', 0),
    compare_three,
    compare_four,
    compare_six
]

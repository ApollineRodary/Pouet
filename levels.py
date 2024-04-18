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
    Explanation('This one was easy! Now, try with 3 colours...', '', 0),
    compare_three,
    Explanation('Nice one. A bit more complicated now with 4 colours!','',0),
    compare_four,
    Explanation('Let us see if you got the trick...','',0),
    compare_six,
    Explanation('This pattern is called the odd-even transposition sorting network. It consists of several columns of comparators. More precisely, to sort a number of colours, we repeat half as many times the following: a first column that covers all wires ("odd step"), and a second column that covers all wires but the top and bottom ones ("even step").','',0),
    Explanation("In this scenario, only colours that are next to each other can be sorted."
                "When that is the case, we cannot build a pattern that uses fewer comparators"
                " than the odd-even transposition sorting network.\n \n"
                "Fun fact: if your pattern can sort a rainbow that is in the reverse order,"
                "it can sort any arrangement of colours, in any order!",'',0)
]

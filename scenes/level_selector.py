from ui.scene import Scene
from objects.button import Button
from scenes.level import Level

LEVELS_PER_ROW = 5
BUTTON_SIZE = 150
BUTTON_SPACING = 50
HORIZONTAL_GRID_MARGIN = (1200 - (BUTTON_SIZE+BUTTON_SPACING) * (LEVELS_PER_ROW-1)) / 2
VERTICAL_GRID_MARGIN = 200

class LevelSelector(Scene):
    def __init__(self):
        self.home_button = Button(
            x=1050, y = 650,
            width = 200, height = 200,
            text = "Back"
        )
        self.level_buttons = []
        super().__init__([self.home_button])

    def add_level(self, level: Level):
        """Adds a level to the level selector"""

        # Find grid position of the level button
        nb_objects = len(self.level_buttons)
        grid_x = nb_objects % LEVELS_PER_ROW
        grid_y = nb_objects // LEVELS_PER_ROW
        button = Button(
            x = HORIZONTAL_GRID_MARGIN + (BUTTON_SIZE+BUTTON_SPACING) * grid_x,
            y = VERTICAL_GRID_MARGIN + (BUTTON_SIZE+BUTTON_SPACING) * grid_y,
            width = BUTTON_SIZE, height = BUTTON_SIZE,
            text = level.name
        )

        # Place button and bind it to the corresponding level
        button.set_command(lambda _: button.canvas.load(level))
        self.level_buttons.append(button)
        self.objects.append(button)

        # Bind the home button of the level to the level selector
        level.home_button.set_command(
            lambda _: level.home_button.canvas.load(self)
        )


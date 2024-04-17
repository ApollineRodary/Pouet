from ui.game_window import GameWindow
window = GameWindow()

from scenes.menu import Menu
from scenes.level_selector import LevelSelector
import levels

menu = Menu()
level_selector = LevelSelector()

menu.start_button.set_command(
    lambda _: window.canvas.load(level_selector)
)
level_selector.home_button.set_command(
    lambda _: window.canvas.load(menu)
)

for level in levels.levels:
    level_selector.add_level(level)

window.canvas.load(menu)
window.mainloop()

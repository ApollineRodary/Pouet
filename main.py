from ui.game_window import GameWindow
from scenes.menu import Menu
from scenes.level import Level
from scenes.level_selector import LevelSelector

window = GameWindow()

menu = Menu()
level_selector = LevelSelector()

menu.start_button.set_command(
    lambda _: window.canvas.load(level_selector)
)
level_selector.home_button.set_command(
    lambda _: window.canvas.load(menu)
)

for i in range(10):
    level_selector.add_level(
        Level(f"Empty level {i+1}"), str(i+1)
    )

window.canvas.load(menu)
window.mainloop()

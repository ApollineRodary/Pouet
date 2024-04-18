from ui.game_window import GameWindow
window = GameWindow()

from scenes.menu import Menu
from scenes.level_selector import LevelSelector
import levels
from scenes.level import Level
import pyglet
from scenes.victory import Victory

pyglet.font.add_file("assets/font/cat_comic/CatComic.ttf")

menu = Menu()
level_selector = LevelSelector()

menu.start_button.set_command(
    lambda _: window.canvas.load(level_selector)
)
level_selector.home_button.set_command(
    lambda _: window.canvas.load(menu)
)

for scene in levels.scenes:
    if isinstance(scene,Level):
        level_selector.add_level(scene)
        level_selector.add_scene(Victory())
    else:
        level_selector.add_scene(scene)
level_selector.scenes[-1].next = menu

window.canvas.load(menu)
window.mainloop()

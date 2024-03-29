from ui.game_window import GameWindow
from scenes.menu import menu

window = GameWindow()
window.canvas.load(menu)
window.mainloop()

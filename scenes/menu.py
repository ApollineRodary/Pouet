from ui.scene import Scene
from objects.button import Button

start_button = Button(
    x = 600, y = 300,
    width = 500, height = 100,
    text = "Start game"
)
quit_button = Button(
    x = 600, y = 500,
    width = 500, height = 100,
    text = "Quit game",
    command = lambda _: exit()
)

menu = Scene([
    start_button,
    quit_button
])

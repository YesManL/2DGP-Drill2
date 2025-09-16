from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

while (x < 780):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)

while (y < 560):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(780, y)
    y = y + 2
    delay(0.01)

while (x > 10):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 560)
    x = x - 2
    delay(0.01)

while (y > 90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(10, y)
    y = y - 2
    delay(0.01)

while (x < 400):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)

while ()

close_canvas()

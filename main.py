import dearpygui.dearpygui as dpg
import time
import math
from snake import Snake
from vector import *


class Game:
    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title='Custom Title', width=1280, height=720)
        dpg.maximize_viewport()
        dpg.setup_dearpygui()

        with dpg.window(tag="Primary Window"):
            dpg.add_text("Hello, world")

        dpg.set_primary_window("Primary Window", True)

    def run(self):
        dpg.show_viewport()

        player = Snake(PyVector2D(640, 320))






        # Game Loop
        while dpg.is_dearpygui_running():

            dt = dpg.get_frame_rate() / 1000
            # insert here any code you would like to run in the render loop
            # you can manually stop by using stop_dearpygui()



            player.input(dt)
            player.move(dt)
            player.draw()
            dpg.render_dearpygui_frame()


        dpg.destroy_context()


if __name__ == '__main__':
    snake = Game()
    snake.run()




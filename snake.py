import dearpygui.dearpygui as dpg
from vector import PyVector2D

class Snake:
    def __init__(self, position: PyVector2D):
        self.position = position

        self.speed = 5






    def update(self, deltatime):
        self.input(deltatime)
        self.draw()

    def draw(self):
        with dpg.window():
            with dpg.drawlist(width=1280, height=720, parent='viewport_back'):
                dpg.draw_circle((self.position.x, self.position.y), 15, color=(255, 255, 255, 255))



    def input(self, deltatime):
        if dpg.is_key_down(dpg.mvKey_W):
            print('Moving Up')
            self.position.y -= 3 * deltatime + self.speed

        if dpg.is_key_down(dpg.mvKey_S):
            print('Moving Down')
            self.position.y += 3 * deltatime + self.speed

        if dpg.is_key_down(dpg.mvKey_D):
            print('Moving Right')
            self.position.x += 3 * deltatime + self.speed

        if dpg.is_key_down(dpg.mvKey_A):
            print('Moving Left')
            self.position.x -= 3 * deltatime + self.speed

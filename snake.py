import dearpygui.dearpygui as dpg
from vector import PyVector2D

class Snake:
    def __init__(self, position: PyVector2D):
        self.position = position
        self. direction = PyVector2D()
        self.speed = 5

    def draw(self):
        with dpg.window(width=1280, height=720):
            with dpg.drawlist(width=1280, height=720):
                dpg.draw_circle((self.position.x, self.position.y), 15, color=(255, 255, 255, 255), fill=(50, 255, 255, 255), label='snake')



    def input(self, deltatime):
        # Move Up (w)
        if dpg.is_key_down(dpg.mvKey_W):
            #self.position.y -= 1 * deltatime + self.speed
            self.direction.y = -1
            self.direction.x = 0
        # Move Down (s)
        if dpg.is_key_down(dpg.mvKey_S):
            #self.position.y += 1 * deltatime + self.speed
            self.direction.y = 1
            self.direction.x = 0
        # Move Right (d)
        if dpg.is_key_down(dpg.mvKey_D):
            #self.position.x += 1 * deltatime + self.speed
            self.direction.x = 1
            self.direction.y = 0
        # Move Left (a)
        if dpg.is_key_down(dpg.mvKey_A):
            #self.position.x -= 1 * deltatime + self.speed
            self.direction.x = -1
            self.direction.y = 0


    def move(self, deltatime):
        if self.direction.x == 1:
            self.position.x += 1 * deltatime + self.speed
        if self.direction.x == -1:
            self.position.x -= 1 * deltatime + self.speed
        if self.direction.y == 1:
            self.position.y += 1 * deltatime + self.speed
        if self.direction.y == -1:
            self.position.y -= 1 * deltatime + self.speed



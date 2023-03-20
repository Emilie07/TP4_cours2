#Emilie Mancera

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.AFRICAN_VIOLET, arcade.color.AMARANTH_PINK, arcade.color.ARYLIDE_YELLOW, arcade.color.BLEU_DE_FRANCE]

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1"):
        super().__init__(width, height)
        self.liste.balles = []
        self.liste.rectangles = []
        def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            pass
        pass

def balle(self):
    for _ in range (20)

    def setup(self):
        pass

    def on_update(self, delta_time: float):
        if balle_x < rayon.cercles:
            balle_x *= -1
        if balle_x > SCREEN_WIDTH - rayon_balle:
            balle_x *= -1
        if balle_y < rayon.cercles:
            balle_y *= -1
        if balle_y > SCREEN_HEIGHT - rayon_balle:
            balle_y *= -1

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(10,10,20, (255, 54, 34))

def rectangle(self):
    def setup(self):
        pass

    def on_update(self delta_time: float):
        pass

def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()

main()
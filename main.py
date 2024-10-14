# This file was created by: Desmond Moran
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from sprites import*
import random

class Game:
    # The game init method initializes all the necessary components for the game, including video and sound
    # this includes the game clock which allows us to set the framerate
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tetris")
        self.clock = pg.time.Clock()
        self.running = True
        locked_positions = {}
        create_grid(locked_positions)
        change_piece = False
        current_piece = get_shape()
        next_piece = get_shape()
        fall_time = 0
        fall_speed = 0.35
        level_time = 0
    def draw(self):
        self.screen.fill(BLACK)
        pg.display.flip()
    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()
    def new(self):
        self.all_sprites = pg.sprite.Group()
    
    def events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

        # pg.quit()
        # process
    def update(self):
        self.all_sprites.update()
    def draw(surface, grid):
        for i in range(row):
            for j in range(col):
                pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    # draw vertical and horizontal grid lines
            draw_grid(surface)

    
if __name__ == "__main__":
    g = Game()
    # create all game elements with the new method (not function)
    g.new()
    # run the game...
    g.run()
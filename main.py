# this file was created by: Desmond Moran

import pygame as pg 
from settings import *
from sprites import *

class Game: 
    def init(self): 
        pass
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption("My Game")
        self.playing = True
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.player = Player(self, 50, 50)
        self.mob = Mob(self, 0, 0)
        self.wall = Wall(self, WIDTH/2, HEIGHT/2)
        for i in range(6): 
            w = Wall(self, TILESIZE*i, TILESIZE*i)
            print(w.rect.x)



# this is a method
# methods are functions that are part of a class
# the run method runs the game loop
    def run(self):
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

        pg.quit()
    def events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False
    def update(self):
        self.all_sprites.update()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

if __name__ == "__main__":
  g = Game()
  g.new()
  g.run()

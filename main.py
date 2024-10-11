# this file was created by: Desmond Moran

import pygame as pg 
from settings import *
from sprites import *
from tilemap import *
from os import path

'''
Goals:
Rules:
Feedback:
Freedom: 
'''

#create a class for game that has all of its properties 
class Game: 
    def init(self): 
        pass
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption("My Game")
        self.playing = True
# where the game creates the sprites and other factors in the game
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self.game_folder, 'level1.txt'))

    def new(self):
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    Wall(self, col*TILESIZE, row*TILESIZE)
                if tile == 'M':
                    Mob(self, col*TILESIZE, row*TILESIZE)
                if tile == 'P':
                    self.player = Player(self, col*TILESIZE, row*TILESIZE)
                if tile == 'U':
                    Powerup(self, col*TILESIZE, row*TILESIZE)
                if tile == "C":
                    Coin(self, col*TILESIZE, row*TILESIZE)


# this is a method
# methods are functions that are part of a class
# the run method runs the game loop
# updates and draws the screen for the game
    def run(self):
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

        pg.quit()
    # when oyu close/quit the screen the game will stop running
    def events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False
    #  makes sure the sprites are constatly being updated 
    def update(self):
        self.all_sprites.update()
    #  draws the sprites and screen
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('ariel')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)
   
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, "asdfasdasdf", 24, WHITE, WIDTH/2, HEIGHT/3)
        self.draw_text(self.screen, str(self.dt*1000), 24, WHITE, WIDTH/30, HEIGHT/30)
        self.draw_text(self.screen, str(self.player.coins), 24, WHITE, WIDTH-75, HEIGHT/20)

        pg.display.flip()

if __name__ == "__main__":
#   instanciating the game
  g = Game()
#   call the funtions running the game
  g.new()
  g.run()
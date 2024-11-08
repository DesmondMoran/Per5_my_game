from testmain import*
from settings import*
from pygame.sprite import Sprite
import pygame as pg

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, T, L]
colors = [RED, GREEN, BLUE, PINK, YELLOW, ORANGE, PURPLE ]


class Piece(Sprite):
    def __init__(self, game, x, y, shape):
        self.groups = game.all_sprites, game.blocks
        Sprite.__init__(self, self.groups)
        self.game = game
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.x = x
        self.y = y
        self.rotation = 0
        self.rect = pg.Rect(self.x * tilesize, self.y * tilesize, tilesize, tilesize)

    def rotate(self):
        # Rotate the shape
        self.rotation = (self.rotation + 1) % len(self.shape)
    
    def update(self):
        # Update the piece's position based on its velocity
        pass  # You'll add logic here later if you want gravity, etc.

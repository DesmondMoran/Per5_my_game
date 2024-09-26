#File was created by: Desmond Moran
import pygame as pg
from pygame.sprite import Sprite
from random import randint
from settings import*
from main import*

class Player(Sprite): 
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        self.vx, self.vy = 0, 0

    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vy -= self.speed
        if keys[pg.K_s]:
            self.vy += self.speed
        if keys[pg.K_a]:
            self.vx -= self.speed
        if keys[pg.K_d]:
            self.vx += self.speed

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect = self.x
                print("this works")
            else:
                print("not working...for hits")
        else:
            print("not working for dir check")
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.x += self.vx * self.game.dt

        self.rect.x = self.x
        self.collide_with_walls('x')

        self.rect.y = self.y 
        self.collide_with_walls('y')
     

class Mob(Sprite): 
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction_x = 1
        self.direction_y = 1
        self.speed = 20
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.speed *= -1
            self.rect.y += 32
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.colliderect(self.game.player):
            self.game.player.rect.x += -40
            self.speed *= -1
            

class Wall(Sprite): 
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_walls
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self): 
     if self.rect.colliderect(self.game.player):
            self.game.player.rect.x += -1
            self.game.player.rect.y += -1
    pass
    
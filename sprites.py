#File was created by: Desmond Moran
import pygame as pg
from pygame.sprite import Sprite
from random import randint
from settings import*
from main import*

#  create and define player class
class Player(Sprite): 
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 20
        self.coins = 0
        self.vx, self.vy = 0, 0

#  defines player action when keys are pressed
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
                    self.x = hits[0].rect.left - TILESIZE
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
                print("this works")
            
        
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - TILESIZE
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
                print("Collided on x axis")

    def collide_with_stuff(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Powerup":
                self.speed += 75
                print("Powerup")
            if str(hits[0].__class__.__name__) == "Coin":
                self.coins += 1
                print("got coin")
            


    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        if self.rect.x > WIDTH:
            self.x = 0
        elif self.rect.x < 0:
            self.x = WIDTH - TILESIZE
        
        if self.rect.y > HEIGHT:
            self.y = 0
        elif self.rect.y < 0:
            self.y = HEIGHT - TILESIZE


        self.rect.x = self.x
        self.collide_with_walls('x')
        
        self.rect.y = self.y 
        self.collide_with_walls('y')

        self.collide_with_stuff(self.game.all_powerups, True)
        self.collide_with_stuff(self.game.all_coins, True)
        
       
     

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
        self.speed = 20
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.speed *= -1
            self.rect.y += 32
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.colliderect(self.game.player):
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

class Powerup(Sprite):
     def __init__(self, game, x, y):   
        self.groups = game.all_sprites, game.all_powerups
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y  

class Coin(Sprite):
     def __init__(self, game, x, y):   
        self.groups = game.all_sprites, game.all_coins
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y  
    
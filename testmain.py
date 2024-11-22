import pygame as pg
import random
from pygame.sprite import Sprite
from settings import *
from testSprites import *
from os import path


def get_shape(game):
    return Piece(game, 5, 0, random.choice(shapes))

def create_grid(locked_positions={}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()
    
    return score



class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tetris")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        self.grid = create_grid()
        self.current_piece = get_shape(self)  # Create the first piece
        self.next_piece = get_shape(self)    # Create the next piece
        self.score = 0
        self.fall_speed = 0.27  # Speed at which pieces fall
        self.last_score = max_score()  # Get the last score
        self.fall_time = 0  # Time for piece falling

    def new(self):
        self.all_sprites.empty()  # Clear any old sprites
        self.blocks.empty()  # Remove any locked positions
        self.current_piece = get_shape(self)  # Create a new piece

    # def convert_shape_format(self):
    #     positions = []
    #     format = self.shape[self.rotation % len(self.shape)]
 
    #     for i, line in enumerate(format):
    #         row = list(line)
    #         for j, column in enumerate(row):
    #             if column == '0':
    #                 positions.append((self.x + j, self.y + i))
 
    #     for i, pos in enumerate(positions):
    #         positions[i] = (pos[0] - 2, pos[1] - 4)
 
    #     return positions

    def lock_piece(self):
        # Lock the current piece in place
        for pos in convert_shape_format(self.current_piece):
            self.grid[pos[1]][pos[0]] = self.current_piece.color
        self.current_piece = self.next_piece
        self.next_piece = get_shape()

    # def valid_space(self, grid):
    #     accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    #     accepted_positions = [j for sub in accepted_positions for j in sub]
    #     formatted = convert_shape_format(self)
 
    #     for pos in formatted:
    #         if pos not in accepted_positions:
    #             if pos[1] > -1:
    #                 return False
 
    #     return True

    def clear_rows(self):
        # Clear completed rows from the grid
        for i in range(len(self.grid)-1, -1, -1):
            row = self.grid[i]
            if (0, 0, 0) not in row:
                del self.grid[i]  # Remove full row
                self.grid.insert(0, [(0,0,0)] * 10)  # Add an empty row at the top
                self.score += 10  # Add points
    


    def draw_window(self):
        self.screen.fill((0, 0, 0))
        font = pg.font.SysFont('comicsans', 60)
        label = font.render('TETRIS', 1, (255, 255, 255))
        self.screen.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
        self.draw_grid()

    def draw_grid(self):
        sx = top_left_x
        sy = top_left_y
        for i in range(len(self.grid)):
            pg.draw.line(self.screen, (128, 128, 128), (sx, sy + i * 30), (sx + play_width, sy + i * 30))
            for j in range(len(self.grid[i])):
                pg.draw.line(self.screen, (128, 128, 128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))

    def draw_next_shape(self):
        font = pg.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', 1, (255, 255, 255))
        sx = top_left_x + play_width + 50
        sy = top_left_y + play_height / 2 - 100
        format = self.next_piece.shape[self.next_piece.rotation % len(self.next_piece.shape)]
        for i, line in enumerate(format):
            for j, column in enumerate(line):
                if column == '0':
                    pg.draw.rect(self.screen, self.next_piece.color, (sx + j * 30, sy + i * 30, 30, 30), 0)
        self.screen.blit(label, (sx + 10, sy - 30))

    def draw_text_middle(self, text, size, color):
        font = pg.font.SysFont("comicsans", size, bold=True)
        label = font.render(text, 1, color)
        self.screen.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), top_left_y + play_height / 2 - label.get_height() / 2))

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.current_piece.x -= 1
                    if not self.valid_space(self.current_piece):
                        self.current_piece.x += 1
                elif event.key == pg.K_RIGHT:
                    self.current_piece.x += 1
                    if not self.valid_space(self.current_piece):
                        self.current_piece.x -= 1
                elif event.key == pg.K_UP:
                    self.current_piece.rotate()
                    if not self.valid_space(self.current_piece):
                        self.current_piece.rotate()
                elif event.key == pg.K_DOWN:
                    self.current_piece.y += 1
                    if not self.valid_space(self.current_piece):
                        self.current_piece.y -= 1

    def update(self):
        self.fall_time += self.clock.get_rawtime()
        if self.fall_time / 1000 >= self.fall_speed:
            self.fall_time = 0
            self.current_piece.y += 1
            if not self.valid_space(self.current_piece):
                self.current_piece.y -= 1
                self.lock_piece()

    def lock_piece(self):
        for pos in self.current_piece.get_positions():
            x, y = pos
            if y >= 0:
                self.locked_positions[(x, y)] = self.current_piece.color
        self.score += self.clear_rows() * 10
        self.current_piece = self.next_piece
        self.next_piece = self.get_new_piece()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw_window()
            self.draw_next_shape()
            pg.display.update()

            if self.check_lost():
                self.draw_text_middle("YOU LOST!", 80, (255, 255, 255))
                pg.display.update()
                pg.time.delay(1500)
                self.running = False
                self.update_score()

# Main menu that starts the game
def main_menu():
    win = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Tetris')
    game = Game()
    while True:
        win.fill((0, 0, 0))
        game.draw_text_middle('Press Any Key to Play', 60, (255, 255, 255))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                return
            if event.type == pg.KEYDOWN:
                game.run()

if __name__ == "__main__":
    main_menu()
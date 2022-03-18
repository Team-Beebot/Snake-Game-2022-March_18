import time

import pygame as pg
from pygame.locals import *

SIZE = 40                   # size of the block(dimension of that block image).

class Snake:
    def __init__(self,parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pg.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*3
        self.y = [SIZE]*3
        self.direction = 'down'
        self.length = length


    def draw(self):
        self.parent_screen.fill((50, 100, 50))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pg.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
       self.direction = 'right'


    def move_down(self):

       self.direction = 'down'

    def move_up(self):
        self.direction = 'up'

    def slide(self):
        if self.direction == 'up':
            self.y -= 10

        if self.direction == 'down':
            self.y += 10

        if self.direction == 'right':
            self.x += 10

        if self.direction == 'left':
            self.x -= 10


        self.draw()



class Game:
    def __init__(self):
        pg.init()
        self.surface = pg.display.set_mode((1000, 600))
        self.surface.fill((50, 100, 50))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pg.event.get():  # getting all the event from event pacakage.
                if event.type == KEYDOWN:  # getting event functions from local of pygame.
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:  # up key function
                        self.snake.move_up()

                    if event.key == K_DOWN:  # down key function
                        self.snake.move_down()

                    if event.key == K_RIGHT:  # Right key function
                        self.snake.move_right()
                        
                    if event.key == K_LEFT:  # left key function
                       self.snake.move_left()
                        
                elif event.type == QUIT:  # while mouse click cross buttion in window
                    running = False


            self.snake.slide()
            time.sleep(0.2)


if __name__ == "__main__":

    game = Game()
    game.run()









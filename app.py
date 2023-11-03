import pygame
import time

from apple import Apple
# TO DO
# Add relevant imports here
from snake import Snake
from pygame.locals import *
from random import randint


class App:
 
    windowWidth = 800
    windowHeight = 600
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.snake = Snake(1) 
        self.apple = Apple(5,5)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True

        # TO DO
        # Do you want to change the image of the apple and snake in the game?
        self._image_surf = pygame.image.load("block.jpg").convert()
        self._apple_surf = pygame.image.load("block.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.snake.update()

        # TO DO
        # does snake eat apple?

        # does snake collide with the wall?

        # does snake collide with itself?
 
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.snake.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.snake.moveRight()
 
            if (keys[K_LEFT]):
                self.snake.moveLeft()
 
            if (keys[K_UP]):
                self.snake.moveUp()
 
            if (keys[K_DOWN]):
                self.snake.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0);

        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
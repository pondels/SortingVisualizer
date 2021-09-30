# https://www.codegrepper.com/code-examples/python/how+to+make+a+screen+in+python
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame

import random
import pygame
from pygame.locals import *
import time
# import arcade

class Visualizer():

    def __init__(self):

        '''
            Defines the Screen and initializes pygame for the text
        '''

        self.run = True
        WIDTH = 720
        HEIGHT = 1280
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.bar_color = (255, 0, 0)
        pygame.init()

    def time_buffer(self, variable):
        # Checks if there is a slowdown buffer to determine how slow the graph runs

        if variable == 'slow':
            time.sleep(.1)
        elif variable == 'fast':
            pass

    def run_self(self, list, itemOne, itemTwo, speedUp, nameOfAlg, count):

        # Runs the buffer
        if itemTwo != None and not speedUp:
            self.time_buffer("slow")
        else:
            self.time_buffer("fast")
        
        # 'resets' the screen
        self.screen.fill((0, 0, 0))

        # Draws the new graph for every item checked or moved
        for i in range(len(list)):
            check_y = 700 - list[i]*10
            y_extend = list[i]*10
            
            # Changes the bar color to green if the items being checked
            # are found in the list

            if i == itemOne or i == itemTwo:
                self.bar_color = (0, 255, 0)
            else:
                self.bar_color = (255, 0, 0)
            
            font1 = pygame.font.SysFont('chalkduster.ttf', 72)
            img1 = font1.render(f"{nameOfAlg}: " + f"{count}", True, (0, 255, 0))
            self.screen.blit(img1, (20, 20))
            pygame.draw.rect(self.screen, self.bar_color, pygame.Rect(100+(30*i), check_y, 25, y_extend))
            # textsurface = self.font.render(sortingAlg, False, (255, 255, 255))
        pygame.display.update()





# https://www.codegrepper.com/code-examples/python/how+to+make+a+screen+in+python

import random
import pygame
import time
# import arcade

class Visualizer():

    def __init__(self):
        self.run = True
        WIDTH = 720
        HEIGHT = 1280
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.bar_color = (255, 0, 0)
    
    def run_self(self, list):
        self.screen.fill((0, 0, 0))
        for i in range(len(list)):
            check_y = 550 - list[i]*3
            y_extend = list[i]*3
            pygame.draw.rect(self.screen, self.bar_color, pygame.Rect(150+(5*i), check_y, 3, y_extend))
            150, 5-155; 160
        pygame.display.update()
        time.sleep(.01)





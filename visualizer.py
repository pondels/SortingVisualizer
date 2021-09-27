# https://www.codegrepper.com/code-examples/python/how+to+make+a+screen+in+python
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame

import random
import pygame
import time
# import arcade

class Visualizer():

    def __init__(self):
        self.run = True
        WIDTH = 720
        HEIGHT = 1280
        # pygame.font.init()
        # self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.bar_color = (255, 0, 0)
    
    def run_self(self, list):
        self.screen.fill((0, 0, 0))
        for i in range(len(list)):
            check_y = 650 - list[i]*3
            y_extend = list[i]*3
            pygame.draw.rect(self.screen, self.bar_color, pygame.Rect(150+(5*i), check_y, 3, y_extend))
            # textsurface = self.font.render(sortingAlg, False, (255, 255, 255))
        pygame.display.update()
        time.sleep(.01)





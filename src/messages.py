import pygame
from pygame.locals import *

pygame.font.init()
myfont = pygame.font.SysFont("Arial", 10)

def message(message, color):
    m = myfont.render(message, 1, color)
    return m
    
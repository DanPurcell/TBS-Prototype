import pygame
from pygame.locals import *

pygame.font.init()
myfont = pygame.font.SysFont("Arial", 12)

def message(message):
    m = myfont.render(message, 1, (255,255,255))
    return m
    
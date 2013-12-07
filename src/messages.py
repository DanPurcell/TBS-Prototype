import pygame
from pygame.locals import *

pygame.font.init()
myfont = pygame.font.SysFont("monospace", 15)

def message(message):
    m = myfont.render("Some text!", 1, (255,255,255))
    return m
    
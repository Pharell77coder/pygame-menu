import pygame
from constants import *


class Rpg:
    def __init__(self, screen, root):
        pygame.init()
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.SysFont("arial.ttk", 24)
        self.root = root

    def handling(self, event):
        pass

    def draw(self):
        self.screen.fill((250, 250, 250))


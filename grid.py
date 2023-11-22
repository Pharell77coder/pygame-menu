import pygame
from constants import *

class Square:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.margin = 0.5

        self.border = 'black'

    def draw(self, screen, color):
        pygame.draw.rect(screen, self.border, (self.margin + self.x * TILESIZE, self.margin + self.y * TILESIZE, TILESIZE, TILESIZE))
        pygame.draw.rect(screen, color,
                         (self.margin + self.x * TILESIZE + self.margin, self.margin + self.y * TILESIZE + self.margin, TILESIZE - self.margin * 2, TILESIZE - self.margin* 2))

class Grid:
    def __init__(self, screen, font, root):
        pygame.init()
        self.screen = screen
        self.font = font
        self.root = root

    def texte(self, text, pos, color='black', bool=True):
        menu_text = self.font.render(text, bool, color)
        menu_rect = menu_text.get_rect(center=(pos[0], pos[1]))
        self.screen.blit(menu_text, menu_rect)

    def handling(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            click_pos = (mouse_pos[0] // TILESIZE, mouse_pos[1] // TILESIZE)
            print(click_pos)
        elif event.key == pygame.K_RETURN:
             self.root.state = "menu"

    def draw(self):
        self.screen.fill((0, 0, 0))
        col = 7
        row = 9

        self.squares = [[(i, j) for i in range(row)] for j in range(col)]
        self.map = []
        for i in self.squares:
            for j in i:
                self.map.append(Square(j))
        for case in self.map:
            case.draw(self.screen, (255, 255, 255))
        pygame.draw.rect(self.screen, 'white', (0, HEIGHT-TILESIZE*2, WIDTH, TILESIZE*2))
        for i in range(6): self.texte("une variable",(50, 525+(20*i)))

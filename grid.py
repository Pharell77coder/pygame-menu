import pygame
from constants import *

class Square:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

        self.border = 'black'

    def draw(self, screen, color):
        pygame.draw.rect(screen, self.border, (self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE))
        pygame.draw.rect(screen, color,
                         (self.x * TILESIZE + 0.5, self.y * TILESIZE + 0.5, TILESIZE - 0.5, TILESIZE - 0.5))


class Pawn(Square):
    def __init__(self, pos):
        super().__init__(pos)
        self.color = 'grey'
        self.selected = False
        self.border = 'black'
        self.animation = False
        self.current_sprites = 0
        self.sprites = list()
        self.sprites.append('grey')
        self.sprites.append('blue')

    def add_selected(self):
        self.selected = True

    def del_selected(self):
        self.selected = False


    def move(self, value):
        self.x = value[0]
        self.y = value[1]

    def get_pos(self):
        return self.x, self.y

    def animate(self):
        self.animation = True

    def update(self, screen, speed) -> None:
        if self.selected :
            self.color = "red"
        elif not self.selected:
                self.color = "grey"
        if self.animation:
            self.current_sprites += speed

            if self.current_sprites >= len(self.sprites):
                self.current_sprites = 0
                self.animation = False

            self.color = self.sprites[int(self.current_sprites)]

        self.draw(screen, self.color)
class Grid:
    def __init__(self, screen, font, root):
        pygame.init()
        self.screen = screen
        self.font = font
        self.root = root

        self.squares = [(i, j) for i in range(WIDTH//TILESIZE) for j in range(HEIGHT//TILESIZE)]
        self.colors = ['white' for _ in self.squares]
        self.pawn = [Pawn((0, 6)), Pawn((5, 4)), Pawn((3, 7)), Pawn((2, 1))]
        self.last_pawn = None

    def handling(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            click_pos = (mouse_pos[0] // TILESIZE, mouse_pos[1] // TILESIZE)
            for i, pawn in enumerate(self.pawn):
                if pawn.get_pos() == click_pos:
                    if not self.pawn[i].selected:
                        if self.last_pawn is not None:
                            self.last_pawn.del_selected()
                        self.pawn[i].add_selected()
                        last_pawn = self.pawn[i]
                    elif self.pawn[i].selected:
                        self.pawn[i].del_selected()
                        last_pawn = None
                elif self.last_pawn is not None:
                    if (click_pos[0], click_pos[1]) not in [p.get_pos() for p in self.pawn]:
                        self.last_pawn.move(click_pos)
                        self.last_pawn.del_selected()
                        self.last_pawn = None

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for elem in self.pawn:
                if elem.selected:
                    elem.animate()

    def draw(self):
        self.screen.fill((230, 250, 240))

        [Square(square).draw(self.screen, color) for square, color in zip(self.squares, (240, 240, 240))]

        for i in range(HEIGHT // TILESIZE):
            for j in range(WIDTH // TILESIZE):
                for element in self.pawn:
                    position = element.get_pos()
                    if i == position[0] and j == position[1]:
                        element.update(self.screen, 0.1)
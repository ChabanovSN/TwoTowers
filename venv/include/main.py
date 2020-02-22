# -*- coding: utf-8 -*-
import pygame
import game
import sys
import config as cf

pygame.font.init()

font_color = cf.font_color
font_big_color = cf.font_big_color
font = cf.font
fontBig = cf.fontBig

surface_width = cf.surface_width
surface_height = cf.surface_height

surface_menu = cf.surface

pygame.display.set_caption("Две Башни")
background_image = cf.background_menu

start = option = ext = None


def DrawText(text, font, surface_menu, x, y, fnColor):
    textobj = font.render(text, 1, fnColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    return surface_menu.blit(textobj, textrect)


width, _ = font.size('Старт')


def midlText(text):
    width, _ = font.size(text)
    return (surface_width / 2 - width / 2)


if __name__ == "__main__":
    moveS = moveO = moveE = 0
    while True:
        surface_menu.blit(background_image, (0, 0))
        if moveS == 0:
            start = DrawText('Старт', font, surface_menu, midlText('Старт'), (surface_height / 2) - 110, font_color)
        else:
            start = DrawText('Старт', fontBig, surface_menu, midlText('Старт'), (surface_height / 2) - 140,
                             font_big_color)
        if moveO == 0:
            option = DrawText('Опции', font, surface_menu, midlText('Опции'), (surface_height / 2) - 40, font_color)
        else:
            option = DrawText('Опции', fontBig, surface_menu, midlText('Опции'), (surface_height / 2) - 40,
                              font_big_color)
        if moveE == 0:
            ext = DrawText('Выход', font, surface_menu, midlText('Выход'), (surface_height / 2) + 30, font_color)
        else:
            ext = DrawText('Выход', fontBig, surface_menu, midlText('Выход'), (surface_height / 2) + 50, font_big_color)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if ext.collidepoint(pos):
                    sys.exit()
                if start.collidepoint(pos):
                    surface_menu.fill((55, 105, 0))
                    game.mainloop()
            if event.type == pygame.MOUSEMOTION:
                if ext.collidepoint(pos):
                    moveE = 1
                else:
                    moveE = 0
                if start.collidepoint(pos):
                    moveS = 1
                else:
                    moveS = 0
                if option.collidepoint(pos):
                    moveO = 1
                else:
                    moveO = 0

        pygame.display.update()
        pygame.display.flip()

# pygame.display.flip() # всё отобразить

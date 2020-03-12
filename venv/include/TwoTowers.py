# -*- coding: utf-8 -*-
import pygame
import game
import sys
import config as cf
import  Options

pygame.font.init()

font_color = cf.font_color
font_big_color = cf.font_big_color
font = cf.font
fontBig = cf.fontBig

surface_width =  cf.surface_width
surface_height = cf.surface_height
surface_menu = pygame.display.set_mode([cf.surface_widthCONST , cf.surface_heightCONST-200],  pygame.DOUBLEBUF)

pygame.display.set_caption(u"Две башни")
background_menu = cf.background_menu
background_menu = pygame.transform.scale(background_menu, [cf.surface_widthCONST , cf.surface_heightCONST-200])




start = option = ext = None


def DrawText(text, font, surface_menu, x, y, fnColor):
    textobj = font.render(text, 1, fnColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    return surface_menu.blit(textobj, textrect)





def midlText(text,fontS):
    width, _ = fontS.size(text)
    return (surface_width / 2 - width / 2)


if __name__ == "__main__":
    moveS = moveO = moveE = 0
    width = height = 0
    running = 1
    while running:

        surface_menu.blit(background_menu, (0, 0))
        if moveS == 0:
            start = DrawText(u'Старт', font, surface_menu, midlText(u'Старт',font), (surface_height / 2) - 120, font_color)
        else:
            start = DrawText(u'Старт', fontBig, surface_menu, midlText(u'Старт',fontBig), (surface_height / 2) - 150,
                             font_big_color)
        if moveO == 0:
            option = DrawText(u'Опции', font, surface_menu, midlText(u'Опции', font), (surface_height / 2) - 40, font_color)
        else:
            option = DrawText(u'Опции', fontBig, surface_menu, midlText(u'Опции', fontBig), (surface_height / 2) - 40,
                              font_big_color)
        if moveE == 0:
            ext = DrawText(u'Выход', font, surface_menu, midlText(u'Выход', font), (surface_height / 2) + 40, font_color)
        else:
            ext = DrawText(u'Выход', fontBig, surface_menu, midlText(u'Выход', fontBig), (surface_height / 2) + 60, font_big_color)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if ext.collidepoint(pos):
                    sys.exit()
                if start.collidepoint(pos):
                    surface_menu.fill(cf.green)
                    running = 0
                    game.mainloop()
                if option.collidepoint(pos):
                    surface_menu.fill(cf.green)
                    running = 0
                    Options.loopOption()
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

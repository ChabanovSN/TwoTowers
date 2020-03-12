# -*- coding: utf-8 -*-
import pygame
import game
import sys
import config as cf
import TwoTowers

textTowerComp = u'Башня противника                                                                                 '
textTowerUser = u'                                                                                       Ваша башня'


level1Text1 = u'Для победы - уничтожьте башню противника, выбирая карты по очереди:'
level1Text2 = u'Крести и  Пики - нанесут урон башне противника,'
level1Text3 = u'Бубны и  Червы - восстановят собственную башню.'
level1Text4 = u'Свойства карт ЗАВИСЯТ от обладателя карт.'

level2Text1=  u'Для победы - уничтожьте башню противника, выбирая карты по очереди:'
level2Text2=  u'Крести - наносят урон башне противника,'
level2Text3=  u'Бубны - нанесут урон вашей башне,'
level2Text4=  u'Пики - восстановят башню противника,'
level2Text5=  u'Червы - восстановят вашу башню.'
level2Text6 = u'Свойства карт НЕ ЗАВИСЯТ от обладателя карт.'

pygame.font.init()

font_color = cf.font_color
font_big_color = cf.font_big_color

font = cf.font
fontBig = cf.fontBig
fontTutorial = cf.fontTutorial


surface_width =  cf.surface_width
surface_height = cf.surface_height
surface_menu = pygame.display.set_mode([cf.surface_widthCONST , cf.surface_heightCONST-200],  pygame.DOUBLEBUF)

pygame.display.set_caption(u"Две башни")
background_menu = cf.background_menu
background_menu = pygame.transform.scale(background_menu, [cf.surface_widthCONST , cf.surface_heightCONST-200])

def drowOnlineHelp(sreen):
    TwoTowers.DrawText(str(u"Карты противника"), cf.fontTutorial, sreen,
                       TwoTowers.midlText(str(u"Карты противника"), cf.fontTutorial),
                       135, cf.black)
    TwoTowers.DrawText(str(u"Ваши карты"), cf.fontTutorial, sreen,
                       TwoTowers.midlText(str(u"Ваши карты"), cf.fontTutorial),
                       cf.surface_heightCONST-370, cf.red)
    TwoTowers.DrawText(str(textTowerComp), cf.fontTutorial, surface_menu,
                       TwoTowers.midlText(textTowerComp, cf.fontTutorial),
                       cf.surface_heightCONST-350, cf.black)
    TwoTowers.DrawText(str(textTowerUser), cf.fontTutorial, surface_menu,
                       TwoTowers.midlText(textTowerUser, cf.fontTutorial),
                       cf.surface_heightCONST - 350, cf.red)
    if cf.level1:
        TwoTowers.DrawText(str(level1Text1), cf.fontTutorial, surface_menu,
                           TwoTowers.midlText(level1Text1, cf.fontTutorial),
                           (surface_height / 2) - 60, font_color)
        TwoTowers.DrawText(str(level1Text2), cf.fontTutorial, sreen,
                           TwoTowers.midlText(level1Text2, cf.fontTutorial),
                           (surface_height / 2) - 30, cf.black)
        TwoTowers.DrawText(str(level1Text3), cf.fontTutorial, sreen,
                           TwoTowers.midlText(level1Text3, cf.fontTutorial),
                           (surface_height / 2) , cf.red)
        TwoTowers.DrawText(str(level1Text4), cf.fontTutorial, sreen,
                           TwoTowers.midlText(level1Text4, cf.fontTutorial),
                           (surface_height / 2) +30, font_color)
    else:
        TwoTowers.DrawText(str(level2Text1), cf.fontTutorial, surface_menu,
                           TwoTowers.midlText(level2Text1, cf.fontTutorial),
                           (surface_height / 2) - 60, font_color)
        TwoTowers.DrawText(str(level2Text2), cf.fontTutorial, surface_menu,
                           TwoTowers.midlText(level2Text2, cf.fontTutorial),
                           (surface_height / 2) - 40, cf.black)
        TwoTowers.DrawText(str(level2Text3), cf.fontTutorial, surface_menu,
                           TwoTowers.midlText(level2Text3, cf.fontTutorial),
                           (surface_height / 2) - 20, cf.red)
        TwoTowers.DrawText(str(level2Text4), cf.fontTutorial, surface_menu,
                           TwoTowers.midlText(level2Text4, cf.fontTutorial),
                           (surface_height / 2), cf.black)
        TwoTowers.DrawText(str(level2Text5), cf.fontTutorial, surface_menu,
                           TwoTowers.midlText(level2Text5, cf.fontTutorial),
                           (surface_height / 2) +20, cf.red)
        TwoTowers.DrawText(str(level2Text6), cf.fontTutorial, surface_menu,
                           TwoTowers.midlText(level2Text6, cf.fontTutorial),
                           (surface_height / 2) +40, font_color)

start = option = ext = None


def loopOption():
    moveL1 = moveL2 = moveE = 0
    width = height = 0
    running =1
    while running:
        surface_menu.blit(background_menu, (0, 0))

        if moveL1 == 0:
            start1 = TwoTowers.DrawText(u'Уровень в 2 масти', font, surface_menu, TwoTowers.midlText(u'Уровень в 2 масти', font), (surface_height / 2) - 130, font_color)

        else:
            start1 = TwoTowers.DrawText(u'Уровень в 2 масти', fontBig, surface_menu, TwoTowers.midlText(u'Уровень в 2 масти', fontBig), (surface_height / 2) - 140, font_big_color)
            TwoTowers.DrawText(str(level1Text1), cf.fontTutorial, surface_menu, TwoTowers.midlText(level1Text1, cf.fontTutorial),
                           (surface_height / 2) - 205, font_color)
            TwoTowers.DrawText(str(level1Text2), cf.fontTutorial, surface_menu, TwoTowers.midlText(level1Text2, cf.fontTutorial),
                           (surface_height / 2) - 185,  cf.black)
            TwoTowers.DrawText(str(level1Text3), cf.fontTutorial, surface_menu, TwoTowers.midlText(level1Text3, cf.fontTutorial),
                           (surface_height / 2) - 165, cf.red)
            TwoTowers.DrawText(str(level1Text4), cf.fontTutorial, surface_menu,
                               TwoTowers.midlText(level1Text4, cf.fontTutorial),
                               (surface_height / 2) - 150, font_color)
        if moveL2 == 0:
            start2 = TwoTowers.DrawText(u'Уровень в 4 масти', font, surface_menu, TwoTowers.midlText(u'Уровень в 4 масти', font), (surface_height / 2) - 40, font_color)
        else:
            start2 = TwoTowers.DrawText(u'Уровень в 4 масти', fontBig, surface_menu, TwoTowers.midlText(u'Уровень в 4 масти', fontBig), (surface_height / 2) - 40, font_big_color)
            TwoTowers.DrawText(str(level2Text1), cf.fontTutorial, surface_menu,
                               TwoTowers.midlText(level2Text1, cf.fontTutorial),
                               (surface_height / 2) - 225, font_color)
            TwoTowers.DrawText(str(level2Text2), cf.fontTutorial, surface_menu,
                               TwoTowers.midlText(level2Text2, cf.fontTutorial),
                               (surface_height / 2) - 205, cf.black)
            TwoTowers.DrawText(str(level2Text3), cf.fontTutorial, surface_menu,
                               TwoTowers.midlText(level2Text3, cf.fontTutorial),
                               (surface_height / 2) - 185, cf.red)
            TwoTowers.DrawText(str(level2Text4), cf.fontTutorial, surface_menu,
                               TwoTowers.midlText(level2Text4, cf.fontTutorial),
                               (surface_height / 2) - 165, cf.black)
            TwoTowers.DrawText(str(level2Text5), cf.fontTutorial, surface_menu,
                               TwoTowers.midlText(level2Text5, cf.fontTutorial),
                               (surface_height / 2) - 145, cf.red)
            TwoTowers.DrawText(str(level2Text6), cf.fontTutorial, surface_menu,
                               TwoTowers.midlText(level2Text6, cf.fontTutorial),
                               (surface_height / 2) - 125, font_color)


        if moveE == 0:
            ext = TwoTowers.DrawText(u'Выход', font, surface_menu, TwoTowers.midlText(u'Выход', font), (surface_height / 2) + 40, font_color)
        else:
            ext = TwoTowers.DrawText(u'Выход', fontBig, surface_menu, TwoTowers.midlText(u'Выход', fontBig), (surface_height / 2) + 60, font_big_color)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if ext.collidepoint(pos):
                    sys.exit()
                if start1.collidepoint(pos):
                    cf.level1 = 1
                    cf.level2 = 0
                    surface_menu.fill(cf.green)
                    game.mainloop()
                if start2.collidepoint(pos):
                    cf.level1 = 0
                    cf.level2 = 1
                    surface_menu.fill(cf.green)
                    game.mainloop()
            if event.type == pygame.MOUSEMOTION:
                if ext.collidepoint(pos):
                    moveE = 1
                else:
                    moveE = 0
                if start1.collidepoint(pos):
                    moveL1 = 1
                else:
                    moveL1 = 0
                if start2.collidepoint(pos):
                    moveL2 = 1
                else:
                    moveL2 = 0

        pygame.display.update()
        pygame.display.flip()

# pygame.display.flip() # всё отобразить
if __name__ == "__main__":
       loopOption()
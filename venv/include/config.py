# -*- coding: utf-8 -*-
import pygame


pygame.init()

level1 = 1
level2 = 0
# size of main screen
surface_width = 800
surface_height = 600

surface_widthCONST = 800
surface_heightCONST = 800
# позиция карт противника
cartPosCompY = 4
# позиция карт противника
cartPosUserY = 504
# по горизонтали одинаково
cartPos1X = 300
cartPos2X = 356
cartPos3X = 412
cartPos4X = 468

# size of card
sizeCardW = 55
sizeCarH = 92
# height of towers
maxheight = 150
heightC = 150
heightU = 150

#шрифт

font = pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 72)
fontBig = pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 85)
fontSmall= pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 25)
fontTutorial= pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 22)
font_color = (255, 255, 153)
font_big_color = (190, 190, 255)

white = (255,255,255)
black = (0, 0, 0)
red   = (255,0,0)
green = (55, 105, 0)



def newKoefWidth(window_width=surface_widthCONST):
    width_koef =1
    if window_width != 0:
        width_koef =  window_width/surface_widthCONST
    return width_koef

def newKoefHeight(window_height = surface_heightCONST):
     height_koef =1
     if window_height != 0:
       height_koef =  window_height/surface_heightCONST
     return  height_koef



surface = pygame.display.set_mode([surface_width, surface_height],  pygame.DOUBLEBUF)

mark_qu = pygame.image.load('images/qv.jpg').convert()
mark_qu  = pygame.transform.scale(mark_qu , (50,50))
mark_qu.set_colorkey(white)

background_menu = pygame.image.load('images/menu_bk.jpg').convert()

towerC100=pygame.image.load('images/towers/tower100C.png').convert()
towerC100  = pygame.transform.scale(towerC100 , (100,heightC+heightC-20))
towerC100.set_colorkey(white)
towerC75=pygame.image.load('images/towers/tower75C.png').convert()
towerC75  = pygame.transform.scale(towerC75 , (100,heightC+heightC-20))
towerC75.set_colorkey(white)
towerC50=pygame.image.load('images/towers/tower50C.png').convert()
towerC50  = pygame.transform.scale(towerC50 , (100,heightC+heightC-20))
towerC50.set_colorkey(white)
towerC25=pygame.image.load('images/towers/tower25C.png').convert()
towerC25  = pygame.transform.scale(towerC25 , (100,heightC+heightC-20))
towerC25.set_colorkey(white)

#towerU100=pygame.image.load('images/towers/tower100U.jpg').convert()
towerU100=pygame.image.load('images/towers/tower100U.png').convert()
towerU100  = pygame.transform.scale(towerU100 , (100,heightC+heightC-20))
towerU100.set_colorkey(white)
towerU75=pygame.image.load('images/towers/tower75U.png').convert()
towerU75  = pygame.transform.scale(towerU75 , (100,heightC+heightC-20))
towerU75.set_colorkey(white)
towerU50=pygame.image.load('images/towers/tower50U.png').convert()
towerU50  = pygame.transform.scale(towerU50 , (100,heightC+heightC-20))
towerU50.set_colorkey(white)
towerU25=pygame.image.load('images/towers/tower25U.png').convert()
towerU25  = pygame.transform.scale(towerU25 , (100,heightC+heightC-20))
towerU25.set_colorkey(white)


background_game = pygame.image.load('images/bk_fight.png').convert()

import pygame

pygame.init()
# size of main screen
surface_width = 800
surface_height = 600
# позиция карт противника
cartPosCompY = 11
# позиция карт противника
cartPosUserY = 503
# по горизонтали одинаково
cartPos1X = 300
cartPos2X = 351
cartPos3X = 402
cartPos4X = 453

# size of card
sizeCardW = 50
sizeCarH = 80
# height of towers
maxheight = 150
heightC = 150
heightU = 150

#шрифт

font = pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 72)
fontBig = pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 85)

font_color = (255, 255, 153)
font_big_color = (153, 102, 255)
# фоны игры
surface = pygame.display.set_mode([surface_width, surface_height])

background_menu = pygame.image.load('images/menu_bk.jpg').convert()
background_menu  = pygame.transform.scale(background_menu , (surface_width , surface_height))

background_game = pygame.image.load('images/bk_fight.png').convert()
background_game  = pygame.transform.scale(background_game , (surface_width, surface_height-200))
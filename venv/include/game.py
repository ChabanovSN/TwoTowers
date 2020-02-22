import pygame
import cards
import random
import sys
import config as cf

pygame.init()
surface_width = cf.surface_width
surface_height = cf.surface_height
screen = cf.surface
screen.fill((55, 105, 0))
pygame.display.set_caption("Две башни")

clock = pygame.time.Clock()
clock.tick(60)

background_image = cf.background_game


cards_deck = cards.cards_deck
Empty = cards.empty_card

sizeCardW = cf.sizeCardW
sizeCarH = cf.sizeCarH
maxheight = cf.maxheight
heightC = cf.heightC
heightU = cf.heightU


endGame = 0



#отрисовка карты
def fourCards(x , y):
    if len(cards_deck) == 0:
        return screen.blit(pygame.transform.scale(Empty.pyObj, (sizeCardW, sizeCarH)), (x, y)), Empty
    card = random.choice(cards_deck)
    if card in cards_deck:
        cards_deck.remove(card)
        return screen.blit(pygame.transform.scale(card.pyObj, (sizeCardW, sizeCarH)), (x, y)), card

# сообщение о победе
def display_message(user, comp):
    myfont = pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 72)
   # myfont = pygame.font.SysFont("Arial", 80)
    if user > comp:
       width, _ = myfont.size("Вы победили!!!")
       return  myfont.render("Вы победили!!!", 0, (0, 0, 0)),width
    elif user < comp:
       width, _ = myfont.size("Противник победил!!!")
       return  myfont.render("Противник победил!!!", 0, (0, 0, 0)),width
    else:
        width, _ = myfont.size("Нечья!!!")
        return myfont.render("Нечья!!!", 0, (0, 0, 0)),width


# урон и ХП
def hp_damG(card):
    global heightC, heightU, endGame
    # print(card.hpM,card.hpY,card.damageM,card.damageY)
    if heightC + card.hpY < maxheight:
        heightC+= card.hpY
    elif card.hpY > 0:
        heightC = maxheight
    if heightC + card.damageY > 0:
        heightC += card.damageY
    else:
        heightC = 0
        endGame =1
        display_message(heightU, heightC)
          #screen.blit(display_message(height_u, height_c), (20, 100))
    if heightU + card.hpM < maxheight:
        heightU += card.hpM
    elif card.hpM > 0:
        heightU = maxheight

    if heightU + card.damageM > 0:
        heightU += card.damageM
    else:
        heightU = 0
        endGame = 1
        display_message(heightU, heightC)
        #screen.blit(display_message(height_u, height_c), (20, 100))
#заполнение при запуске игры
def firstInit():
    ## init comp cart first
    cartScreen, cartClass = fourCards(cf.cartPos1X, cf.cartPosCompY)
    cartCom1 = WorkCards(cartScreen, cartClass, cf.cartPos1X)
    cartScreen, cartClass = fourCards(cf.cartPos2X, cf.cartPosCompY)
    cartCom2 = WorkCards(cartScreen, cartClass, cf.cartPos2X)
    cartScreen, cartClass = fourCards(cf.cartPos3X, cf.cartPosCompY)
    cartCom3 = WorkCards(cartScreen, cartClass, cf.cartPos3X)
    cartScreen, cartClass = fourCards(cf.cartPos4X, cf.cartPosCompY)
    cartCom4 = WorkCards(cartScreen, cartClass, cf.cartPos4X)
    workCardListComp = [cartCom1, cartCom2, cartCom3, cartCom4]
    ## init user cart first
    cartScreen, cartClass = fourCards(cf.cartPos1X, cf.cartPosUserY)
    cartCom1 = WorkCards(cartScreen, cartClass, cf.cartPos1X)
    cartScreen, cartClass = fourCards(cf.cartPos2X, cf.cartPosUserY)
    cartCom2 = WorkCards(cartScreen, cartClass, cf.cartPos2X)
    cartScreen, cartClass = fourCards(cf.cartPos3X, cf.cartPosUserY)
    cartCom3 = WorkCards(cartScreen, cartClass, cf.cartPos3X)
    cartScreen, cartClass = fourCards(cf.cartPos4X, cf.cartPosUserY)
    cartCom4 = WorkCards(cartScreen, cartClass, cf.cartPos4X)
    workCardListUser = [cartCom1, cartCom2, cartCom3, cartCom4]
    return workCardListComp,workCardListUser
#генерация новой карты
def newCart(listCart, posY,pos):
    for i in range(len(listCart)):
        if listCart[i].objScreenCart.collidepoint(pos):
            hp_damG(listCart[i].cart)
            posX = listCart[i].posX
            cartScreen, cartClass = fourCards(posX, posY)
            listCart[i] = WorkCards(cartScreen, cartClass, posX)
            # print(workCardListComp[i].cart.name, i)

# для контроля положения и состояния (временный класс, может идея будет по лучше)
class WorkCards:
    def __init__(self, objScreenCart, cart, posX):
        self.objScreenCart = objScreenCart
        self.cart = cart
        self.posX = posX

#главный циклы игры
def mainloop():
 global  heightC, heightU
 global endGame
 workCardListComp, workCardListUser = firstInit()
 while True:

    screen.blit(background_image, (0, 100))
    # com's tower
    surf1C = pygame.Surface((50, maxheight))


    surf2C = pygame.Surface((50, maxheight -heightC))
    surf2C.fill((20, 250, 50))
    rect1C = pygame.Rect((20, 218, 50, maxheight))
    rect2C = pygame.Rect((20, 218, 50,  maxheight))

    screen.blit(surf1C, rect1C)
    screen.blit(surf2C, rect2C)
    # users's tower
    surf1U = pygame.Surface((50, maxheight))
    surf2U = pygame.Surface((50,maxheight - heightU))
    surf1U.fill((250, 0, 0))
    surf2U.fill((0, 250, 0))
    rect1U = pygame.Rect((720, 218, 50, maxheight))
    rect2U = pygame.Rect((720, 218, 50, maxheight))

    screen.blit(surf1U, rect1U)
    screen.blit(surf2U, rect2U)
    # comp's cards

    pygame.draw.rect(screen, (0, 0, 0), (300, 8, 205, 85), 3)
    # my cards
    pygame.draw.rect(screen, (255, 0, 0), (300, 500, 205, 85), 3)


    if endGame:
        letter,wightText =display_message(heightU, heightC)
        screen.blit(letter, (surface_width/2 - wightText/2, 100))
    #pygame.display.flip()
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()

          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ## if mouse is pressed get position of cursor ##
            pos = pygame.mouse.get_pos()

            newCart(workCardListComp, cf.cartPosCompY, pos)
            newCart(workCardListUser, cf.cartPosUserY, pos)

            if len(cards_deck) == 0:
                allEmpty = 0
                for c in workCardListComp:
                    if c.cart == Empty:
                        allEmpty +=1
                for c in workCardListUser:
                    if c.cart == Empty:
                        allEmpty +=1
                #print(allEmpty, " All empty")
                if allEmpty == 8: # all list empty
                    endGame = 1



    #pygame.display.update()
    pygame.display.flip()
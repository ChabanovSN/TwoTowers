# -*- coding: utf-8 -*-
import pygame
import cards
import random
import sys
import config as cf
import logic as lg
import time
import TwoTowers
import Options

pygame.init()
surface_width = cf.surface_width
surface_height = cf.surface_height
screen = pygame.display.set_mode([cf.surface_widthCONST, cf.surface_heightCONST],  pygame.DOUBLEBUF)


screen.fill(cf.green)




background_game  = pygame.transform.scale(cf.background_game , [cf.surface_widthCONST , cf.surface_heightCONST-450])
# clock = pygame.time.Clock()
# clock.tick(60)


Empty = cards.empty_card
Back =cards.back_card
maxheight = cf.maxheight

####
towerY = 195
textDemY = 175

towerCompX = 20
textDemCompX = 30


towerUserX = 680
textDemUserX = 700


backGRX = 0
backGRY = 125
####
endGame = 0



#отрисовка карты
def fourCards(x , y,cards_deck):

    if len(cards_deck) == 0:
        return screen.blit(pygame.transform.scale(Empty.pyObj, (cf.sizeCardW, cf.sizeCarH)), (x, y)), Empty
    card = random.choice(cards_deck)
    if card in cards_deck:
        cards_deck.remove(card)
        obj =screen.blit(pygame.transform.scale(card.pyObj, (cf.sizeCardW, cf.sizeCarH)), (x, y))
        drawTextDamgEachCards(card,x,y)
        pygame.display.flip()

        return obj, card


def drawTextDamgEachCards(cart,x,y):
    moveY = y
    if surface_height / 2 > y:
        moveY += cf.sizeCarH+4
    else:
        x +=5
        moveY -= cf.sizeCarH/3-2
    text = 0
    fnColor = None
    if cart.hpM != 0:
        if cf.level2:
            fnColor = cf.red
        else:
            if surface_height / 2 < y: # текст для компа
                fnColor = cf.red
            else:
                fnColor = cf.black
        text =cart.hpM
    elif cart.damageM != 0:
        # только для 2 уровня
        text = cart.damageM
        fnColor = cf.red
    elif cart.hpY != 0:
        # только для 2 уровня
        fnColor = cf.black
        text = cart.hpY
    else:
        if cf.level2:
            fnColor = cf.black
        else:
            if surface_height / 2 < y: # текст для компа
                fnColor = cf.black
            else:
                fnColor = cf.red
        text = cart.damageY


    text = text/maxheight * 100
    text = round(text, 1)
    pygame.draw.rect(screen, cf.green, (x, moveY,cf.sizeCardW,25))

    pygame.display.flip()
    width, _ = cf.fontTutorial.size(str(text))
    textobj = cf.fontTutorial.render(str(text), 0, fnColor)

    screen.blit(textobj, (x,  moveY))


# сообщение о победе
def display_message(user, comp):

    if user > comp:
        width, _ = cf.font.size(u"Вы победили!!!")
        return  cf.font.render(u"Вы победили!!!", 0, cf.black),width
    elif user < comp:
        width, _ = cf.font.size(u"Противник победил!!!")
        return  cf.font.render(u"Противник победил!!!", 0, cf.black),width
    else:
        width, _ = cf.font.size(u"Ничья!!!")
        return cf.font.render(u"Ничья!!!", 0, cf.black),width


# урон и ХП
def hp_damG(card,heightU,heightC,whoSpet):
    global  endGame
    if cf.level2 :
        if heightC + card.hpY < maxheight:

            heightC += card.hpY
        elif card.hpY > 0:
            heightC = maxheight
        if heightC + card.damageY > 0:

            heightC += card.damageY
        else:
            heightC = 0
            endGame =1
            display_message(heightU, heightC)

        if heightU + card.hpM < maxheight:
            heightU+= card.hpM
        elif card.hpM > 0:
            heightU= maxheight

        if heightU + card.damageM > 0:
            heightU+= card.damageM
        else:
            heightU = 0
            endGame = 1
            display_message(heightU, heightC)

    else:   # level1 whoStep = 1 ходит комп
        if whoSpet:
            if heightC + card.hpM < maxheight: # комп лечет себя
                heightC += card.hpM
            elif card.hpM > 0:
                heightC = maxheight

            if heightU + card.damageY > 0: # комп бьет меня
                heightU += card.damageY
            else:
                heightU = 0
                endGame = 1
                display_message(heightU, heightC)

        else:           #whoStep = 0 ходит игрок
            if heightU + card.hpM < maxheight:
                heightU += card.hpM
            elif card.hpM > 0:
                heightU = maxheight

            if heightC + card.damageY > 0:  # комп бьет меня
                heightC += card.damageY
            else:
                heightC = 0
                endGame = 1
                display_message(heightU, heightC)

    return heightU, heightC

#заполнение при запуске игры
def firstInit(cards_deck):
    ## init comp cart first
    cartScreen, cartClass = fourCards(cf.cartPos1X, cf.cartPosCompY,cards_deck)
    cartCom1 = WorkCards(cartScreen, cartClass, cf.cartPos1X)
    cartScreen, cartClass = fourCards(cf.cartPos2X, cf.cartPosCompY,cards_deck)
    cartCom2 = WorkCards(cartScreen, cartClass, cf.cartPos2X)
    cartScreen, cartClass = fourCards(cf.cartPos3X, cf.cartPosCompY,cards_deck)
    cartCom3 = WorkCards(cartScreen, cartClass, cf.cartPos3X)
    cartScreen, cartClass = fourCards(cf.cartPos4X, cf.cartPosCompY,cards_deck)
    cartCom4 = WorkCards(cartScreen, cartClass, cf.cartPos4X)

    workCardListComp = [cartCom1, cartCom2, cartCom3, cartCom4]
    ## init user cart first
    cartScreen, cartClass = fourCards(cf.cartPos1X, cf.cartPosUserY,cards_deck)
    cartCom1 = WorkCards(cartScreen, cartClass, cf.cartPos1X)
    cartScreen, cartClass = fourCards(cf.cartPos2X, cf.cartPosUserY,cards_deck)
    cartCom2 = WorkCards(cartScreen, cartClass, cf.cartPos2X)
    cartScreen, cartClass = fourCards(cf.cartPos3X, cf.cartPosUserY,cards_deck)
    cartCom3 = WorkCards(cartScreen, cartClass, cf.cartPos3X)
    cartScreen, cartClass = fourCards(cf.cartPos4X, cf.cartPosUserY,cards_deck)
    cartCom4 = WorkCards(cartScreen, cartClass, cf.cartPos4X)
    workCardListUser = [cartCom1, cartCom2, cartCom3, cartCom4]
    return workCardListComp,workCardListUser
#генерация новой карты
def newCart(listCart, posY,pos,heightU, heightC,cards_deck,whoStep):
    for i in range(len(listCart)):

        if listCart[i].objScreenCart.collidepoint(pos):

            heightU, heightC = hp_damG(listCart[i].cart, heightU, heightC,whoStep)
            posX = listCart[i].posX
            cartScreen, cartClass = fourCards(posX, posY,cards_deck)
            listCart[i] = WorkCards(cartScreen, cartClass, posX)
            return  heightU, heightC
            # print(workCardListComp[i].cart.name, i)

# для контроля положения и состояния (временный класс, может идея будет по лучше)
class WorkCards:
    def __init__(self, objScreenCart, cart, posX):
        self.objScreenCart = objScreenCart
        self.cart = cart
        self.posX = posX

def textDemage(hieght):
    if hieght/maxheight * 100 >= maxheight:
        demhieght = 100
    else:
        demhieght = hieght/maxheight * 100
    demhieght = round(demhieght,1)
    time.sleep(0.2)  # для визуального замедления  хода компа
    return cf.fontSmall.render(str(demhieght), 0, cf.font_big_color)

def drawMoveChooseCart(listCart,posY, pos):

    moveY = posY
    if surface_height/2 > posY:
        moveY +=cf.sizeCarH + 35
    else:
        moveY -= cf.sizeCarH +30
    for i in range(len(listCart)):
        if listCart[i].objScreenCart.collidepoint(pos):
            screen.blit(pygame.transform.scale(Back.pyObj, (cf.sizeCardW, cf.sizeCarH)), (listCart[i].posX, posY))
            pygame.display.flip()

            screen.blit(pygame.transform.scale(listCart[i].cart.pyObj, (cf.sizeCardW, cf.sizeCarH)), (listCart[i].posX, moveY))
            pygame.display.flip()
            time.sleep(0.5)


#главный циклы игры
def mainloop():
    if cf.level1:
        pygame.display.set_caption(u"Две башни - игра в 2 масти")
    else:
        pygame.display.set_caption(u"Две башни - игра в 4 масти")
    heightC = cf.heightC
    heightU = cf.heightU
    cards_deck = cards.get_cards_deck()
    global endGame, backGRX, backGRY,towerCompX, towerY,textDemCompX, textDemY,towerUserX,textDemUserX
    workCardListComp, workCardListUser = firstInit(cards_deck)
    step = 0 #  переключатель ходов между игроком и компом
    drawHelp = 0 # отрисовка справки
    while True:

        screen.blit(background_game, (backGRX, backGRY))
        mark_qb_obj = screen.blit(cf.mark_qu, (cf.surface_widthCONST - 50, 0))

        # com's tower
        screen.blit(lg.getTower(heightC, 0),(towerCompX, towerY))
        screen.blit(textDemage(heightC), (textDemCompX, textDemY))
        # users's tower

        screen.blit(lg.getTower(heightU, 1),(towerUserX,towerY))
        screen.blit(textDemage(heightU), (textDemUserX, textDemY))
        # comp's cards
        pygame.draw.rect(screen, (0, 0, 0), (300, 0, 225, 100), 3) # рамка для карт компа
        # my cards
        userRect = pygame.draw.rect(screen, (255, 0, 0), (300, 500, 225, 100), 3) # рамка для карт игрока
        if endGame:
            letter,wightText =display_message(heightU, heightC)
            screen.blit(letter, (surface_width/2 - wightText/2, 100))
            start = TwoTowers.DrawText(u'Рестарт', cf.font, screen, TwoTowers.midlText(u'Рестарт', cf.font), (surface_height / 2) - 110, cf.font_color)
            option = TwoTowers.DrawText(u'Сменить сложность', cf.font, screen, TwoTowers.midlText(u'Сменить сложность', cf.font),
                                        (surface_height / 2) , cf.font_color)
            ext = TwoTowers.DrawText(u'Выход', cf.font, screen, TwoTowers.midlText(u'Выход', cf.font), (surface_height / 2)+110, cf.font_color)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if ext.collidepoint(pos):
                        sys.exit()
                    if start.collidepoint(pos):
                        endGame = 0
                        step = 0
                        mainloop()
                    if option.collidepoint(pos):
                        endGame = 0
                        step = 0
                        Options.loopOption()
                if event.type == pygame.MOUSEMOTION:
                    if start.collidepoint(pos):
                        TwoTowers.DrawText(u'Рестарт', cf.font, screen, TwoTowers.midlText(u'Рестарт', cf.font), (surface_height / 2) - 110, cf.font_big_color)
                    if option.collidepoint(pos):
                         TwoTowers.DrawText(u'Сменить сложность', cf.font, screen, TwoTowers.midlText(u'Сменить сложность', cf.font), (surface_height / 2), cf.font_big_color)
                    if ext.collidepoint(pos) :
                        TwoTowers.DrawText(u'Выход', cf.font, screen, TwoTowers.midlText(u'Выход', cf.font),(surface_height / 2) + 110, cf.font_big_color)
        #pygame.display.flip()
        if step == 1 and endGame == 0:  # ходит комп
            step = 0
            posChooseCart = lg.chooseRightCart(workCardListComp, heightC, heightU)  # передаем карты и состояние башен в logic.py файл
            pos = (posChooseCart.posX, cf.cartPosCompY)
            drawMoveChooseCart(workCardListComp, cf.cartPosCompY, pos)
            time.sleep(0.5)# для визуального замедления  хода компа
            heightU, heightC = newCart(workCardListComp, cf.cartPosCompY, pos,heightU, heightC,cards_deck,1)  # и возвращаем  выбранную логикой карту

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                if step == 0 and userRect.collidepoint(pos) and endGame == 0: #ходит игрок
                    step = 1
                    drawMoveChooseCart(workCardListUser, cf.cartPosUserY, pos)
                    time.sleep(0.5)
                    heightU, heightC = newCart(workCardListUser, cf.cartPosUserY, pos, heightU, heightC, cards_deck,0)
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if mark_qb_obj.collidepoint(pos):
                    drawHelp = 1
                else:
                    drawHelp = 0
        if drawHelp:
            Options.drowOnlineHelp(screen)  # справка
        if len(cards_deck) == 0:  # проверка на пустую колоду
            allEmpty = 0
            for c in workCardListComp:
                if c.cart == Empty:
                    allEmpty += 1
            for c in workCardListUser:
                if c.cart == Empty:
                     allEmpty += 1
            if allEmpty == 8:  # all list empty
               endGame = 1
               step = 1

        #pygame.display.update()
        pygame.display.flip()
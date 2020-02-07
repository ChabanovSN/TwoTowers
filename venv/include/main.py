import pygame
import cards
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((55, 105, 0))
pygame.display.set_caption("Две башни")

clock = pygame.time.Clock()
clock.tick(60)

background_image = cards.background_image
background_image = pygame.transform.scale(background_image, (800, 400))
screen.blit(background_image, (0, 100))
cards_deck = cards.cards_deck
Empty = cards.empty_card

sizeCardW = 50
sizeCarH = 80
maxheight = 150
heightC = 150
heightU = 150
runnig = 1

c1 = c2 = c3 = c4 = u1 = u2 = u3 = u4 = None
cardc1 = cardc2 = cardc3 = cardc4 = cardu1 = cardu2 = cardu3 = cardu4 = None


def fourCards(x, y):
    if len(cards_deck) == 0:
        return screen.blit(pygame.transform.scale(Empty.pyObj, (sizeCardW, sizeCarH)), (x, y)), Empty
    card = random.choice(cards_deck)
    if card in cards_deck:
        cards_deck.remove(card)
        return screen.blit(pygame.transform.scale(card.pyObj, (sizeCardW, sizeCarH)), (x, y)), card


def display_message(user, comp):
    myfont = pygame.font.SysFont("Arial", 80)
    if user > comp:
        letter = myfont.render("Вы победили!!!", 0, (0, 0, 0))
    elif user < comp:
        letter = myfont.render("Противник победил!!!", 0, (0, 0, 0))
    else:
        letter = myfont.render("Нечья!!!", 0, (0, 0, 0))
    screen.blit(letter, (20, 100))


def hp_damG(card, height_u, height_c):
    # print(card.hpM,card.hpY,card.damageM,card.damageY)
    if height_c + card.hpY < maxheight:
        height_c += card.hpY
    elif card.hpY > 0:
        height_c = maxheight
    if height_c + card.damageY > 0:
        height_c += card.damageY
    else:
        height_c = 0
        display_message(height_u, height_c)

    if height_u + card.hpM < maxheight:
        height_u += card.hpM
    elif card.hpM > 0:
        height_u = maxheight

    if height_u + card.damageM > 0:
        height_u += card.damageM
    else:
        height_u = 0
        display_message(height_u, height_c)

    return height_c, height_u


while runnig:

    # com's tower
    surf1C = pygame.Surface((50, maxheight))
    surf1C.fill((0, 250, 0))
    surf2C = pygame.Surface((50, heightC))
    rect1C = pygame.Rect((20, 218, 50, maxheight))
    rect2C = pygame.Rect((20, 218, 50, maxheight))

    screen.blit(surf1C, rect1C)
    screen.blit(surf2C, rect2C)
    # users's tower
    surf1U = pygame.Surface((50, maxheight))
    surf2U = pygame.Surface((50, heightU))
    surf1U.fill((0, 255, 0))
    surf2U.fill((255, 0, 0))
    rect1U = pygame.Rect((720, 218, 50, maxheight))
    rect2U = pygame.Rect((720, 218, 50, maxheight))

    screen.blit(surf1U, rect1U)
    screen.blit(surf2U, rect2U)
    # comp's cards   
    pygame.draw.rect(screen, (0, 0, 0), (300, 8, 205, 85), 3)
    if c1 == None:
        c1, cardc1 = fourCards(300, 11)
    if c2 == None:
        c2, cardc2 = fourCards(351, 11)
    if c3 == None:
        c3, cardc3 = fourCards(402, 11)
    if c4 == None:
        c4, cardc4 = fourCards(453, 11)

    # my cards
    pygame.draw.rect(screen, (255, 0, 0), (300, 500, 205, 85), 3)
    if u1 == None:
        u1, cardu1 = fourCards(300, 503)
    if u2 == None:
        u2, cardu2 = fourCards(351, 503)
    if u3 == None:
        u3, cardu3 = fourCards(402, 503)
    if u4 == None:
        u4, cardu4 = fourCards(453, 503)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = 0
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ## if mouse is pressed get position of cursor ##
            pos = pygame.mouse.get_pos()
            ## check if cursor is on button ##
            if c1.collidepoint(pos):
                heightC, heightU = hp_damG(cardc1, heightU, heightC)
                c1, cardc1 = fourCards(300, 11)
            if c2.collidepoint(pos):
                heightC, heightU = hp_damG(cardc2, heightU, heightC)
                c2, cardc2 = fourCards(351, 11)
            if c3.collidepoint(pos):
                heightC, heightU = hp_damG(cardc3, heightU, heightC)
                c3, cardc3 = fourCards(402, 11)
            if c4.collidepoint(pos):
                heightC, heightU = hp_damG(cardc4, heightU, heightC)
                c4, cardc4 = fourCards(453, 11)
            if u1.collidepoint(pos):
                heightC, heightU = hp_damG(cardu1, heightU, heightC)
                u1, cardu1 = fourCards(300, 503)
            if u2.collidepoint(pos):
                heightC, heightU = hp_damG(cardu2, heightU, heightC)
                u2, cardu2 = fourCards(351, 503)
            if u3.collidepoint(pos):
                heightC, heightU = hp_damG(cardu3, heightU, heightC)
                u3, cardu3 = fourCards(402, 503)
            if u4.collidepoint(pos):
                heightC, heightU = hp_damG(cardu4, heightU, heightC)
                u4, cardu4 = fourCards(452, 503)
            if cardc1 == Empty and cardc2 == Empty and cardc3 == Empty and cardc4 == Empty and \
                    cardu2 == Empty and cardu2 == Empty and cardu3 == Empty and cardu4 == Empty:
                display_message(heightU, heightC)

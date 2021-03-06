# -*- coding: utf-8 -*-
import config as cf

maxheight = cf.maxheight

hearts = []
spades = []
clubs = []
diamonds = []


def chooseRightCart(list, heightTowerComp, heightTowerUser):
    del spades[:]
    del diamonds[:]
    del clubs[:]
    del hearts[:]
    fourCardSuit(list)  # забиваем карты по масти и сортируем
    # printCart("H",hearts)
    # printCart("D", diamonds)
    # printCart("C", clubs)
    # printCart("S",spades)
    # print("-----------------------")
    if heightTowerComp < maxheight / 2:  # если башня компа разрушенна на половину
        if cf.level2:
            if len(spades) > 0:  # лечим башну
                crt = spades[0]
                return crt
            if len(diamonds) > 0:  # если не можем лечить тогда разрушаем башню игрока
                crt = diamonds[0]
                return crt

            if len(clubs) > 0:  # если не можем разрушить рушем башню компа
                crt = clubs[0]
                return crt

            if len(hearts) > 0:  # если не можем разрушить лечим башню игрока
                crt = hearts[0]
                return crt
        else:
            if len(hearts) > 0:  # лечим башну
                crt = hearts[0]
                return crt
            if len(diamonds) > 0:  # лечим башну
                crt = diamonds[0]
                return crt
            if len(spades) > 0:  # fight
                crt = spades[0]
                return crt
            if len(clubs) > 0:  # fight
                crt = clubs[0]
                return crt
    else:  # if hp > 50 %
        if cf.level2:
            if len(diamonds) > 0:  # fight user
                crt = diamonds[0]
                return crt
            if len(spades) > 0:  # hp comp
                crt = spades[0]
                return crt
            if len(hearts) > 0:  # hp user
                crt = hearts[0]
                return crt
            if len(clubs) > 0:  # fight comp
                crt = clubs[0]
                return crt


        else:  # level1
            if len(clubs) > 0:  # fight
                crt = clubs[0]
                return crt
            if len(spades) > 0:  # fight
                crt = spades[0]
                return crt
            if len(diamonds) > 0:  # hp
                crt = diamonds[0]
                return crt
            if len(hearts) > 0:  # hp
                crt = hearts[0]
                return crt


def fourCardSuit(list):
    for cartClass in list:
        if cartClass.cart.name.startswith("H"):
            hearts.append(cartClass)
        elif cartClass.cart.name.startswith("S"):
            spades.append(cartClass)
        elif cartClass.cart.name.startswith("C"):
            clubs.append(cartClass)
        elif cartClass.cart.name.startswith("D"):
            diamonds.append(cartClass)
    sortCard()


def sortCard():
    if len(clubs) != 0:
        if cf.level2:
            clubs.sort(key=sortSecond, reverse=True)  # Ace last
        else:
            clubs.sort(key=sortSecond, reverse=False)  # Ace first
    if len(hearts) != 0:
        if cf.level2:
            hearts.sort(key=sortSecond, reverse=False)  # Ace last
        else:
            hearts.sort(key=sortSecond, reverse=True)  # Ace first
    if len(spades) != 0:
        if cf.level2:
            spades.sort(key=sortSecond, reverse=True)  # Ace first
        else:
            spades.sort(key=sortSecond, reverse=False)  # Ace first
    if len(diamonds) != 0:
        if cf.level2:
            diamonds.sort(key=sortSecond, reverse=False)  # Ace first
        else:
            diamonds.sort(key=sortSecond, reverse=True)  # Ace first


def sortSecond(cartClass):
    if cartClass.cart.hpM != 0:
        return cartClass.cart.hpM
    if cartClass.cart.damageM != 0:
        return cartClass.cart.damageM
    if cartClass.cart.hpY != 0:
        return cartClass.cart.hpY
    if cartClass.cart.damageY != 0:
        return cartClass.cart.damageY


def getTower(height, user):
    if user:
        if height > 75:
            return cf.towerU100
        if height > 50:
            return cf.towerU75
        if height > 10:
            return cf.towerU50
        else:
            return cf.towerU25
    else:
        if height > 75:
            return cf.towerC100
        if height > 50:
            return cf.towerC75
        if height > 10:
            return cf.towerC50
        else:
            return cf.towerC25


# debuf
def printCart(c, list):
    for i in list:
        print(c, i.cart.name)

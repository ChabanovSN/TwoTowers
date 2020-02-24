import config as cf

maxheight = cf.maxheight

hearts   =[]
spades    =[]
clubs    =[]
diamonds = []

def chooseRightCart( list, heightTowerComp,heightTowerUser):

    fourCardSuit(list)# забиваем карты по масти и сортируем
    if heightTowerComp < maxheight/2: # если башня компа разрушенна на половину
        if len(spades) > 0: # лечим башну
            crt  = spades[0]
            spades.clear()
            return crt
        if len(diamonds) > 0: # если не можем лечить тогда разрушаем башню игрока
            crt = diamonds[0]
            diamonds.clear()
            return crt

        if len(clubs) >0:  # если не можем разрушить рушем башню компа
            crt = clubs[0]
            clubs.clear()
            return crt

        if len(hearts) > 0:  # если не можем разрушить лечим башню игрока
            crt = hearts[0]
            hearts.clear()
            return crt
    else: # если ХР башни компа больше 50%
        if len(diamonds) >0:  # разрушаем башню игрока
            crt = diamonds[0]
            diamonds.clear()
            return crt
        if len(clubs) >0:  # если не можем разрушить рушем башню компа
            crt = clubs[0]
            clubs.clear()
            return crt
        if len(spades) > 0:  # лечим башну компа
            crt = spades[0]
            spades.clear()
            return crt
        if len(hearts) > 0:  # если не можем разрушить лечим башню игрока
            crt = hearts[0]
            hearts.remove(crt)
            return crt



def fourCardSuit(list):
    for cartClass in list:
        if cartClass.cart.name.startswith("H"):
            hearts.append(cartClass)
        elif  cartClass.cart.name.startswith("S"):
            spades.append(cartClass)
        elif cartClass.cart.name.startswith("C"):
            clubs.append(cartClass)
        elif cartClass.cart.name.startswith("D"):
            diamonds.append(cartClass)
    sortCard()

def sortCard():
    if len(clubs) != 0:
        clubs.sort(key=sortSecond, reverse=True)  # Ace last

    if len(hearts) !=0:
        hearts.sort(key=sortSecond, reverse=False)# Ace last

    if len(spades) != 0:
        spades.sort(key=sortSecond, reverse=True)# Ace first

    if len(diamonds) != 0:
        diamonds.sort(key=sortSecond, reverse=False) # Ace first



def sortSecond(cartClass):
    if cartClass.cart.hpM != 0:
        return cartClass.cart.hpM
    if cartClass.cart.damageM != 0:
        return cartClass.cart.damageM
    if cartClass.cart.hpY != 0:
        return cartClass.cart.hpY
    if cartClass.cart.damageY != 0:
        return cartClass.cart.damageY
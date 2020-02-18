import pygame
import random

pygame.init()
pygame.display.set_mode((0, 0))

background_image = pygame.image.load('images/bk_fight.png').convert()


class Card:
    def __init__(self, name, hpM, damageM, hpY, damageY, path):
        """Constructor"""
        self.name = name
        self.hpM = hpM
        self.damageM = damageM
        self.hpY = hpY
        self.damageY = damageY
        self.pyObj = pygame.image.load(path).convert()


empty_card = Card("Empty", 0, 0, 0, 0, 'images/empty.jpg')

# hpM, damageM - мои  hpY, damageY - компа
# CUBS
CAce = Card("CAce", 0, 0, 0, -50, 'images/clubs/CAce.jpg')
CKing = Card("CKing", 0, 0, 0, -34, 'images/clubs/CKing.jpg')
CLady = Card("CLady", 0, 0, 0, -33, 'images/clubs/CLady.jpg')
CJack = Card("CJack", 0, 0, 0, -32, 'images/clubs/CJack.jpg')
C10 = Card("C10", 0, 0, 0, -30, 'images/clubs/C10.jpg')
C9 = Card("C9", 0, 0, 0, -27, 'images/clubs/C9.jpg')
C8 = Card("C8", 0, 0, 0, -24, 'images/clubs/C8.jpg')
C7 = Card("C7", 0, 0, 0, -21, 'images/clubs/C7.jpg')
C6 = Card("C6", 0, 0, 0, -16, 'images/clubs/C6.jpg')
C5 = Card("C5", 0, 0, 0, -13, 'images/clubs/C5.jpg')
C4 = Card("C4", 0, 0, 0, -10, 'images/clubs/C4.jpg')
C3 = Card("C3", 0, 0, 0, -8, 'images/clubs/C3.jpg')
C2 = Card("C2", 0, 0, 0, -5, 'images/clubs/C2.jpg')
# hpM, damageM - мои  hpY, damageY - компа
# SPADES
SAce = Card("SAce", 0, 0, 50, 0, 'images/spades/SAce.jpg')
SKing = Card("SKing", 0, 0, 34, 0, 'images/spades/SKing.jpg')
SLady = Card("SLady", 0, 0, 33, 0, 'images/spades/SLady.jpg')
SJack = Card("SJack", 0, 0, 32, 0, 'images/spades/SJack.jpg')
S10 = Card("S10", 0, 0, 30, 0, 'images/spades/S10.jpg')
S9 = Card("S9", 0, 0, 27, 0, 'images/spades/S9.jpg')
S8 = Card("S8", 0, 0, 24, 0, 'images/spades/S8.jpg')
S7 = Card("S7", 0, 0, 21, 0, 'images/spades/S7.jpg')
S6 = Card("S6", 0, 0, 16, 0, 'images/spades/S6.jpg')
S5 = Card("S5", 0, 0, 13, 0, 'images/spades/S5.jpg')
S4 = Card("S4", 0, 0, 10, 0, 'images/spades/S4.jpg')
S3 = Card("S3", 0, 0, 8, 0, 'images/spades/S3.jpg')
S2 = Card("S2", 0, 0, 5, 0, 'images/spades/S2.jpg')
# hpM, damageM - мои  hpY, damageY - компа
# HEARTS
HAce = Card("HAce", 50, 0, 0, 0, 'images/hearts/HAce.jpg')
HKing = Card("HKing", 34, 0, 0, 0, 'images/hearts/HKing.jpg')
HLady = Card("HLady", 33, 0, 0, 0, 'images/hearts/HLady.jpg')
HJack = Card("HJack", 32, 0, 0, 0, 'images/hearts/HJack.jpg')
H10 = Card("H10", 30, 0, 0, 0, 'images/hearts/H10.jpg')
H9 = Card("H9", 27, 0, 0, 0, 'images/hearts/H9.jpg')
H8 = Card("H8", 24, 0, 0, 0, 'images/hearts/H8.jpg')
H7 = Card("H7", 21, 0, 0, 0, 'images/hearts/H7.jpg')
H6 = Card("H6", 16, 0, 0, 0, 'images/hearts/H6.jpg')
H5 = Card("H5", 13, 0, 0, 0, 'images/hearts/H5.jpg')
H4 = Card("H4", 10, 0, 0, 0, 'images/hearts/H4.jpg')
H3 = Card("H3", 8, 0, 0, 0, 'images/hearts/H3.jpg')
H2 = Card("H2", 5, 0, 0, 0, 'images/hearts/H2.jpg')
# hpM, damageM - мои  hpY, damageY - компа
# DIAMONDS
DAce = Card("DAce", 0, -50, 0, 0, 'images/diamonds/DAce.jpg')
DKing = Card("DKing", 0, -34, 0, 0, 'images/diamonds/DKing.jpg')
DLady = Card("DLady", 0, -33, 0, 0, 'images/diamonds/DLady.jpg')
DJack = Card("DJack", 0, -32, 0, 0, 'images/diamonds/DJack.jpg')
D10 = Card("D10", 0, -30, 0, 0, 'images/diamonds/D10.jpg')
D9 = Card("D9", 0, -27, 0, 0, 'images/diamonds/D9.jpg')
D8 = Card("D8", 0, -24, 0, 0, 'images/diamonds/D8.jpg')
D7 = Card("D7", 0, -21, 0, 0, 'images/diamonds/D7.jpg')
D6 = Card("D6", 0, -21, 0, 0, 'images/diamonds/D6.jpg')
D5 = Card("D5", 0, -13, 0, 0, 'images/diamonds/D5.jpg')
D4 = Card("D4", 0, -10, 0, 0, 'images/diamonds/D4.jpg')
D3 = Card("D3", 0, -8, 0, 0, 'images/diamonds/D3.jpg')
D2 = Card("D2", 0, -5, 0, 0, 'images/diamonds/D2.jpg')


cards_deck = [
    CAce, CLady, CJack, C10, C9, C8, C7, C6, C5, C4, C3, C2,
    SAce, SLady, SJack, S10, S9, S8, S7, S6, S5, S4, S3, S2,
    HAce, HLady, HJack, H10, H9, H8, H7, H6, H5, H4, H3, H2,
    DAce, DLady, DJack, D10, D9, D8, D7, D6, D5, D4, D3, D2
]

if __name__ == "__main__":
    rd = random.choice(cards_deck)
    print(rd.name)
# for p in cards_deck: print(p.name)

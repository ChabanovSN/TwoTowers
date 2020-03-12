# -*- coding: utf-8 -*-
import os
import pygame
import random


pygame.init()
pygame.display.set_mode((0, 0))



class Card:
    def __init__(self, name, hpM, damageM, hpY, damageY, path):
        """Constructor"""
        self.name = name
        self.hpM = hpM
        self.damageM = damageM
        self.hpY = hpY
        self.damageY = damageY
        self.pyObj = pygame.image.load(os.path.join(path)).convert()



empty_card = Card("Empty", 0, 0, 0, 0, 'images/empty.jpg')
back_card  = Card("Back", 0, 0, 0, 0, 'images/rubashka.jpg')

# hpM, damageM - мои  hpY, damageY - компа
# CLUBS
CAce = Card("CAce", 0, 0, 0, -50, 'images/clubs/CAce.TGA')
CKing = Card("CKing", 0, 0, 0, -34, 'images/clubs/CKing.TGA')
CLady = Card("CLady", 0, 0, 0, -33, 'images/clubs/CLady.TGA')
CJack = Card("CJack", 0, 0, 0, -32, 'images/clubs/CJack.TGA')
C10 = Card("C10", 0, 0, 0, -30, 'images/clubs/C10.TGA')
C9 = Card("C9", 0, 0, 0, -27, 'images/clubs/C9.TGA')
C8 = Card("C8", 0, 0, 0, -24, 'images/clubs/C8.TGA')
C7 = Card("C7", 0, 0, 0, -21, 'images/clubs/C7.TGA')
C6 = Card("C6", 0, 0, 0, -16, 'images/clubs/C6.TGA')
C5 = Card("C5", 0, 0, 0, -13, 'images/clubs/C5.TGA')
C4 = Card("C4", 0, 0, 0, -10, 'images/clubs/C4.TGA')
C3 = Card("C3", 0, 0, 0, -8, 'images/clubs/C3.TGA')
C2 = Card("C2", 0, 0, 0, -5, 'images/clubs/C2.TGA')

# hpM, damageM - мои  hpY, damageY - компа
# SPADES
SAce = Card("SAce", 0, 0, 50, 0, 'images/spades/SAce.TGA')
SKing = Card("SKing", 0, 0, 34, 0, 'images/spades/Sking.TGA')
SLady = Card("SLady", 0, 0, 33, 0, 'images/spades/SLady.TGA')
SJack = Card("SJack", 0, 0, 32, 0, 'images/spades/SJack.TGA')
S10 = Card("S10", 0, 0, 30, 0, 'images/spades/S10.TGA')
S9 = Card("S9", 0, 0, 27, 0, 'images/spades/S9.TGA')
S8 = Card("S8", 0, 0, 24, 0, 'images/spades/S8.TGA')
S7 = Card("S7", 0, 0, 21, 0, 'images/spades/S7.TGA')
S6 = Card("S6", 0, 0, 16, 0, 'images/spades/S6.TGA')
S5 = Card("S5", 0, 0, 13, 0, 'images/spades/S5.TGA')
S4 = Card("S4", 0, 0, 10, 0, 'images/spades/S4.TGA')
S3 = Card("S3", 0, 0, 8, 0, 'images/spades/S3.TGA')
S2 = Card("S2", 0, 0, 5, 0, 'images/spades/S2.TGA')
# hpM, damageM - мои  hpY, damageY - компа
# HEARTS
HAce = Card("HAce", 50, 0, 0, 0, 'images/hearts/HAce.TGA')
HKing = Card("HKing", 34, 0, 0, 0, 'images/hearts/HKing.TGA')
HLady = Card("HLady", 33, 0, 0, 0, 'images/hearts/HLady.TGA')
HJack = Card("HJack", 32, 0, 0, 0, 'images/hearts/HJack.TGA')
H10 = Card("H10", 30, 0, 0, 0, 'images/hearts/H10.TGA')
H9 = Card("H9", 27, 0, 0, 0, 'images/hearts/H9.TGA')
H8 = Card("H8", 24, 0, 0, 0, 'images/hearts/H8.TGA')
H7 = Card("H7", 21, 0, 0, 0, 'images/hearts/H7.TGA')
H6 = Card("H6", 16, 0, 0, 0, 'images/hearts/H6.TGA')
H5 = Card("H5", 13, 0, 0, 0, 'images/hearts/H5.TGA')
H4 = Card("H4", 10, 0, 0, 0, 'images/hearts/H4.TGA')
H3 = Card("H3", 8, 0, 0, 0, 'images/hearts/H3.TGA')
H2 = Card("H2", 5, 0, 0, 0, 'images/hearts/H2.TGA')
# hpM, damageM - мои  hpY, damageY - компа
# DIAMONDS
DAce = Card("DAce", 0, -50, 0, 0, 'images/diamonds/DAce.TGA')
DKing = Card("DKing", 0, -34, 0, 0, 'images/diamonds/DKing.TGA')
DLady = Card("DLady", 0, -33, 0, 0, 'images/diamonds/DLady.TGA')
DJack = Card("DJack", 0, -32, 0, 0, 'images/diamonds/DJack.TGA')
D10 = Card("D10", 0, -30, 0, 0, 'images/diamonds/D10.TGA')
D9 = Card("D9", 0, -27, 0, 0, 'images/diamonds/D9.TGA')
D8 = Card("D8", 0, -24, 0, 0, 'images/diamonds/D8.TGA')
D7 = Card("D7", 0, -21, 0, 0, 'images/diamonds/D7.TGA')
D6 = Card("D6", 0, -21, 0, 0, 'images/diamonds/D6.TGA')
D5 = Card("D5", 0, -13, 0, 0, 'images/diamonds/D5.TGA')
D4 = Card("D4", 0, -10, 0, 0, 'images/diamonds/D4.TGA')
D3 = Card("D3", 0, -8, 0, 0, 'images/diamonds/D3.TGA')
D2 = Card("D2", 0, -5, 0, 0, 'images/diamonds/D2.TGA')




def get_cards_deck():
    return [
     CAce, CLady, CJack, C10, C9, C8, C7, C6, C5, C4, C3, C2,
     SAce, SLady, SJack, S10, S9, S8, S7, S6, S5, S4, S3, S2,
     HAce, HLady,  HJack, H10, H9, H8, H7, H6, H5, H4, H3, H2,
     DAce, DLady, DJack, D10, D9, D8, D7, D6, D5, D4, D3, D2
]

if __name__ == "__main__":
    rd = random.choice(get_cards_deck())
    print(rd.name)
# for p in cards_deck: print(p.name)

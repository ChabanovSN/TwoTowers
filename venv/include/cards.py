# -*- coding: utf-8 -*-
import os
import pygame
import random
import config as cf

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

#### LEVEL 1
# hpM, damageM - мои  hpY, damageY - компа
# CLUBS
CAce1 = Card("CAce", 0, 0, 0, -50, 'images/clubs/CAce.TGA')
CKing1 = Card("CKing", 0, 0, 0, -34, 'images/clubs/CKing.TGA')
CLady1 = Card("CLady", 0, 0, 0, -33, 'images/clubs/CLady.TGA')
CJack1 = Card("CJack", 0, 0, 0, -32, 'images/clubs/CJack.TGA')
C101 = Card("C10", 0, 0, 0, -30, 'images/clubs/C10.TGA')
C91 = Card("C9", 0, 0, 0, -27, 'images/clubs/C9.TGA')
C81 = Card("C8", 0, 0, 0, -24, 'images/clubs/C8.TGA')
C71 = Card("C7", 0, 0, 0, -21, 'images/clubs/C7.TGA')
C61 = Card("C6", 0, 0, 0, -16, 'images/clubs/C6.TGA')
C51 = Card("C5", 0, 0, 0, -13, 'images/clubs/C5.TGA')
C41 = Card("C4", 0, 0, 0, -10, 'images/clubs/C4.TGA')
C31 = Card("C3", 0, 0, 0, -8, 'images/clubs/C3.TGA')
C21 = Card("C2", 0, 0, 0, -5, 'images/clubs/C2.TGA')

# hpM, damageM - мои  hpY, damageY - компа
# SPADES
SAce1 = Card("SAce", 0, 0, 0, -50, 'images/spades/SAce.TGA')
SKing1 = Card("SKing", 0, 0, 0, -34, 'images/spades/Sking.TGA')
SLady1 = Card("SLady", 0, 0, 0, -33, 'images/spades/SLady.TGA')
SJack1 = Card("SJack", 0, 0, 0, -32, 'images/spades/SJack.TGA')
S101 = Card("S10", 0, 0, 0, -30, 'images/spades/S10.TGA')
S91 = Card("S9", 0, 0, 0, -27, 'images/spades/S9.TGA')
S81 = Card("S8", 0, 0, 0, -24, 'images/spades/S8.TGA')
S71 = Card("S7", 0, 0, 0, -21, 'images/spades/S7.TGA')
S61 = Card("S6", 0, 0, 0, -16, 'images/spades/S6.TGA')
S51 = Card("S5", 0, 0, 0, -13, 'images/spades/S5.TGA')
S41 = Card("S4", 0, 0, 0, -10, 'images/spades/S4.TGA')
S31 = Card("S3", 0, 0, 0, -8, 'images/spades/S3.TGA')
S21 = Card("S2", 0, 0, 0, -5, 'images/spades/S2.TGA')
# hpM, damageM - мои  hpY, damageY - компа
# HEARTS
HAce1 = Card("HAce", 50, 0, 0, 0, 'images/hearts/HAce.TGA')
HKing1 = Card("HKing", 34, 0, 0, 0, 'images/hearts/HKing.TGA')
HLady1 = Card("HLady", 33, 0, 0, 0, 'images/hearts/HLady.TGA')
HJack1 = Card("HJack", 32, 0, 0, 0, 'images/hearts/HJack.TGA')
H101 = Card("H10", 30, 0, 0, 0, 'images/hearts/H10.TGA')
H91 = Card("H9", 27, 0, 0, 0, 'images/hearts/H9.TGA')
H81 = Card("H8", 24, 0, 0, 0, 'images/hearts/H8.TGA')
H71 = Card("H7", 21, 0, 0, 0, 'images/hearts/H7.TGA')
H61 = Card("H6", 16, 0, 0, 0, 'images/hearts/H6.TGA')
H51 = Card("H5", 13, 0, 0, 0, 'images/hearts/H5.TGA')
H41 = Card("H4", 10, 0, 0, 0, 'images/hearts/H4.TGA')
H31 = Card("H3", 8, 0, 0, 0, 'images/hearts/H3.TGA')
H21 = Card("H2", 5, 0, 0, 0, 'images/hearts/H2.TGA')
# hpM, damageM - мои  hpY, damageY - компа
# DIAMONDS
DAce1 = Card("DAce", 50, 0, 0, 0, 'images/diamonds/DAce.TGA')
DKing1 = Card("DKing", 34, 0, 0, 0, 'images/diamonds/DKing.TGA')
DLady1 = Card("DLady", 33, 0, 0, 0, 'images/diamonds/DLady.TGA')
DJack1 = Card("DJack", 32, 0, 0, 0, 'images/diamonds/DJack.TGA')
D101 = Card("D10", 30, 0, 0, 0, 'images/diamonds/D10.TGA')
D91 = Card("D9", 27, 0, 0, 0, 'images/diamonds/D9.TGA')
D81 = Card("D8", 24, 0, 0, 0, 'images/diamonds/D8.TGA')
D71 = Card("D7", 21, 0, 0, 0, 'images/diamonds/D7.TGA')
D61 = Card("D6", 16, 0, 0, 0, 'images/diamonds/D6.TGA')
D51 = Card("D5", 13, 0, 0, 0, 'images/diamonds/D5.TGA')
D41 = Card("D4", 10, 0, 0, 0, 'images/diamonds/D4.TGA')
D31 = Card("D3", 8, 0, 0, 0, 'images/diamonds/D3.TGA')
D21 = Card("D2", 5, 0, 0, 0, 'images/diamonds/D2.TGA')






#### LEVEL 2
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
D6 = Card("D6", 0, -16, 0, 0, 'images/diamonds/D6.TGA')
D5 = Card("D5", 0, -13, 0, 0, 'images/diamonds/D5.TGA')
D4 = Card("D4", 0, -10, 0, 0, 'images/diamonds/D4.TGA')
D3 = Card("D3", 0, -8, 0, 0, 'images/diamonds/D3.TGA')
D2 = Card("D2", 0, -5, 0, 0, 'images/diamonds/D2.TGA')




def get_cards_deck():
    if cf.level1:
        return [
            CAce1, CLady1, CJack1, C101, C91, C81, C71, C61, C51, C41, C31, C21,
            SAce1, SLady1, SJack1, S101, S91, S81, S71, S61, S51, S41, S31, S21,
            HAce1, HLady1, HJack1, H101, H91, H81, H71, H61, H51, H41, H31, H21,
            DAce1, DLady1, DJack1, D101, D91, D81, D71, D61, D51, D41, D31, D21
        ]
    elif cf.level2:
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

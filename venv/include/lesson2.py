import pygame
import random
import sys

class Spark:
    def __init__(self, x ,y,width ):
        self.x = x
        self.y = y
        self.width = width
        self.dx = (random.random() - 0.5) * 5
        self.dy = (random.random() - 0.5) * 5
    def Update(self):
        self.x = self.x +self.dx
        self.y = self.y +self.dy
        self.dy +=0.05
    def Draw(self, screen):
        pygame.draw.line(screen,(255,255,0),[self.x,self.y],[self.x+self.width,self.y+self.width],self.width)



pygame.init()
surface_width = 800
surface_height = 600
screen = pygame.display.set_mode((surface_width, surface_height ))

myfont = pygame.font.Font('fonts/GUERRILLA-Normal.ttf', 72)

def main_window():
    clock = pygame.time.Clock()
    objects = []
    dt=0
    global  screen

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif   event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                objects.append(Spark(mx ,my ,5))
        dt = clock.tick(60)
        screen.fill((55, 105, 0))
        screen.blit(myfont.render(str(dt), 0, (0, 0, 0)),(100,100))
        for  ob in objects:
             ob.Update()
             ob.Draw(screen)


        pygame.display.flip()
if __name__ == "__main__":
    main_window()
import pygame
from game import practiceGame, rankedGame
from Screens.menu import drawMenu
from Constants import *

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
font = pygame.font.Font('freesansbold.ttf', 32)
fontSmall = pygame.font.Font('freesansbold.ttf', 25)

HEIGHT = 500
WIDTH = 700
FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def mainMenu():
    run = True
    clock = pygame.time.Clock()


    while run:
            
                
        ev = pygame.event.get()

        for event in ev:

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pos[0] >= 250 and pos[0] <= 450) and (pos[1] >= 320 and pos[1] <= 370):
                    print('CLICKED Practice')
                    practiceGame()
                
                elif (pos[0] >= 250 and pos[0] <= 450) and (pos[1] >= 400 and pos[1] <= 450):
                    print('CLICKED RANKED')
                    rankedGame()

            elif event.type == pygame.QUIT:
                run = False
                break

        drawMenu(WINDOW)
        clock.tick(FPS)
        
        
    pygame.quit()

if __name__ == '__main__':
    mainMenu()
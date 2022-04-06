import pygame
from Constants.constants import LIMITS
pygame.init()

pygame.display.set_caption("PONG")

#screen dimensions
WIDTH = LIMITS["right"]
HEIGHT = LIMITS["down"]
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = LIMITS["fps"]



GREEN = (194,234,189)
PINK = (237,37,78)
YELLOW = (249,220,92)
BLUE = (1,25,54)
GREY = (70,83,98)


SCORE_FONT = pygame.font.SysFont("comicsans", 50)
font = pygame.font.Font('freesansbold.ttf', 32)
fontSmall = pygame.font.Font('freesansbold.ttf', 25)

def drawMenu(window):
    window.fill(GREEN)
    pygame.draw.rect(WINDOW, YELLOW, pygame.Rect(250, 320, 200, 50))
    pygame.draw.rect(WINDOW, YELLOW, pygame.Rect(250, 400, 200, 50))

    text = font.render('Welcome To Pong', True, PINK)
    WINDOW.blit(text, [200, 100])

    rankedText = fontSmall.render('Ranked', True, PINK)
    WINDOW.blit(rankedText, [280, 420])

    FreeText = fontSmall.render('Free Play', True, PINK)
    WINDOW.blit(FreeText, [280, 340])
    pygame.display.flip()


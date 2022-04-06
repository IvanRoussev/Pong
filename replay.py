import pygame
pygame.init()

pygame.display.set_caption("PONG")

#screen dimensions


WIDTH = 700
HEIGHT = 500
FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


GREEN = (194,234,189)
PINK = (237,37,78)
YELLOW = (249,220,92)
BLUE = (1,25,54)
GREY = (70,83,98)


SCORE_FONT = pygame.font.SysFont("comicsans", 50)
font = pygame.font.Font('freesansbold.ttf', 32)
fontSmall = pygame.font.Font('freesansbold.ttf', 25)

def drawReplay(window):
    window.fill(GREEN)
    pygame.draw.rect(WINDOW, YELLOW, pygame.Rect(250, 320, 200, 50))
    pygame.draw.rect(WINDOW, YELLOW, pygame.Rect(250, 400, 200, 50))

    text = font.render('GameOver', True, PINK)
    WINDOW.blit(text, [260, 100])

    rankedText = fontSmall.render('Exit', True, PINK)
    WINDOW.blit(rankedText, [320, 420])

    FreeText = fontSmall.render('PlayAgain', True, PINK)
    WINDOW.blit(FreeText, [280, 340])
    pygame.display.flip()


def mainReplay():
    run = True

    clock = pygame.time.Clock()


    while run:
            
                
        drawReplay(WINDOW)
        clock.tick(FPS)
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (pos[0] >= 250 and pos[0] <= 450) and (pos[1] >= 320 and pos[1] <= 370):
                    print('---CLICKED PLAY AGAIN---')
                    mainMenu()


                elif (pos[0] >= 250 and pos[0] <= 450) and (pos[1] >= 400 and pos[1] <= 450):
                    run = False
                    break
                    
            
            if event.type == pygame.QUIT:
                run = False
                break
        
    pygame.quit()

if __name__ == '__main__':
    mainReplay()
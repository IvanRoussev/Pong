import pygame
from Constants.constants import LIMITS
pygame.init()

pygame.display.set_caption("PONG")


#screen dimensions
WIDTH = LIMITS["right"]
HEIGHT = LIMITS["down"]
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = LIMITS["fps"]


#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (194,234,189)
PINK = (237,37,78)
YELLOW = (249,220,92)
BLUE = (1,25,54)
GREY = (70,83,98)

#Sprite Dimensions
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
BALL_RADIUS = 7

#Score required to win
WINNING_SCORE = 2

# FONTS
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
font = pygame.font.Font('freesansbold.ttf', 32)
fontSmall = pygame.font.Font('freesansbold.ttf', 25)



#Sprite for Paddle 
class Paddle:
    COLOR = PINK
    VEL = 10

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


#Sprite for Ball 
class Ball:
    MAX_VEL = 5
    COLOR = BLUE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.radius)


    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1




#draw window for Ranked GAME!!!!, paddle, ball, left_score, right_score
def drawRanked(window, paddles, ball, left_score, right_score):
    window.fill(GREEN)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, GREY)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, GREY)
    window.blit(left_score_text, (600, 30))
    window.blit(right_score_text, (100, 30))


    for paddle in paddles:
        paddle.draw(window)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, YELLOW, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    ball.draw(window)
    pygame.display.update()

def drawPractice(window, paddles, ball):
    window.fill(GREEN)

    for paddle in paddles:
        paddle.draw(window)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, YELLOW, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    ball.draw(window)
    pygame.display.update()

# Collision between ball and top wall bottom wall and paddles
def handleCollision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1     

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = ball.y - middle_y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = ball.y - middle_y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel

#move paddles
def paddleMove(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move(up=True)
    if keys[pygame.K_s]:
        left_paddle.move(up=False)

    if keys[pygame.K_UP]:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN]:
        right_paddle.move(up=False)




def rankedGame():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0


    while run:
        drawRanked(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        keys = pygame.key.get_pressed()
        paddleMove(keys, left_paddle, right_paddle)
        ball.move()
        handleCollision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            left_score +=1
            ball.reset()

        elif ball.x > WIDTH:
            right_score +=1
            ball.reset()

        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Right player Wins"

        elif right_score >= WINNING_SCORE:
            won = True 
            win_text = "Left Player Wins"


        if won:
            text = SCORE_FONT.render(win_text, 1, GREY)
            WINDOW.blit(text, (200, 200))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

        
    pygame.quit()



def practiceGame():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)



    while run:
        drawPractice(WINDOW, [left_paddle, right_paddle], ball)
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        keys = pygame.key.get_pressed()
        paddleMove(keys, left_paddle, right_paddle)
        ball.move()
        handleCollision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            ball.reset()

        elif ball.x > WIDTH:
            ball.reset()

        
    pygame.quit()

import pygame
import sys
import random


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("BOUNCE GAME")

clock = pygame.time.Clock()


ballImage = pygame.image.load("ball.png").convert_alpha()
successSound = pygame.mixer.Sound("boing.wav")

font = pygame.font.SysFont(None, 36)


ballRect = ballImage.get_rect()

MAX_X = WINDOW_WIDTH - ballRect.width
MAX_Y = WINDOW_HEIGHT - ballRect.height

ballRect.left = random.randrange(MAX_X)
ballRect.top = random.randrange(MAX_Y)

xSpeed = 3
ySpeed = 3


score = 0
MAX_SCORE = 5
gameOver = False

startTime = pygame.time.get_ticks()
endTime = None


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

            mouseX, mouseY = event.pos

            # Player clicked the ball
            if ballRect.collidepoint(mouseX, mouseY):

                score += 1
                successSound.play()

                # Move ball to new random position
                ballRect.left = random.randrange(MAX_X)
                ballRect.top = random.randrange(MAX_Y)


                xIncrease = random.randint(1, 5)
                yIncrease = random.randint(1, 5)

                xSpeed = (abs(xSpeed) + xIncrease) * (1 if xSpeed > 0 else -1)
                ySpeed = (abs(ySpeed) + yIncrease) * (1 if ySpeed > 0 else -1)


                if score == MAX_SCORE:
                    gameOver = True
                    endTime = pygame.time.get_ticks()


    if not gameOver:

        ballRect.left += xSpeed
        ballRect.top += ySpeed


        if ballRect.left <= 0 or ballRect.right >= WINDOW_WIDTH:
            xSpeed = -xSpeed

        if ballRect.top <= 0 or ballRect.bottom >= WINDOW_HEIGHT:
            ySpeed = -ySpeed


    window.fill(BLACK)

   
    scoreText = font.render("Score: " + str(score), True, WHITE)
    window.blit(scoreText, (10, 10))

  
    if not gameOver:
        window.blit(ballImage, ballRect)

    
    if gameOver:

        totalTime = (endTime - startTime) / 1000

        winText = font.render("Game Over!", True, WHITE)
        timeText = font.render(
            "Time: " + str(round(totalTime, 2)) + " seconds", True, WHITE
        )

        window.blit(winText, (WINDOW_WIDTH//2 - 70, WINDOW_HEIGHT//2 - 20))
        window.blit(timeText, (WINDOW_WIDTH//2 - 120, WINDOW_HEIGHT//2 + 20))

    pygame.display.update()
    clock.tick(FPS)
import pygame
import random
import sys
import math

pygame.init()

# window stuff
screenWidth = 640
screenHeight = 480
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Too Many Balls")
clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# load beach ball image
ballImageOriginal = pygame.image.load("ball.png").convert_alpha()

# ball settings
ballList = []
minRadius = 12
maxRadius = 24

# game variables
score = 0
lastSeconds = 0
startTicks = pygame.time.get_ticks()
gameOver = False

def create_ball():
    r = random.randint(minRadius, maxRadius)

    x = random.randint(r, screenWidth - r)
    y = random.randint(r, screenHeight - r)

    size = r * 2
    img = pygame.transform.smoothscale(ballImageOriginal, (size, size))

    # random velocity
    vx = random.choice([-3, -2, 2, 3])
    vy = random.choice([-3, -2, 2, 3])

    return [x, y, r, img, vx, vy]

# starting ball
ballList.append(create_ball())

running = True
while running:

    clock.tick(60)
    window.fill(WHITE)

    currentTicks = pygame.time.get_ticks()
    secondsElapsed = (currentTicks - startTicks) // 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

            mouseX, mouseY = pygame.mouse.get_pos()
            hitIndex = -1

            for i, ball in enumerate(ballList):
                bx, by, br, img, vx, vy = ball
                dist = math.hypot(mouseX - bx, mouseY - by)

                if dist <= br:
                    hitIndex = i
                    break

            if hitIndex >= 0:
                score += 1
                ballList.pop(hitIndex)

    if not gameOver:

        # spawn balls each second
        if secondsElapsed > lastSeconds:
            for _ in range(secondsElapsed - lastSeconds):
                ballList.append(create_ball())
            lastSeconds = secondsElapsed

        for ball in ballList:

            bx, by, br, img, vx, vy = ball

            # move ball
            bx += vx
            by += vy

            # bounce off walls
            if bx - br <= 0 or bx + br >= screenWidth:
                vx = -vx

            if by - br <= 0 or by + br >= screenHeight:
                vy = -vy

            # update values
            ball[0] = bx
            ball[1] = by
            ball[4] = vx
            ball[5] = vy

            rect = img.get_rect(center=(bx, by))
            window.blit(img, rect)

        draw_text(window, "Score: " + str(score), 10, 10, BLACK, 24)
        draw_text(window, "Seconds: " + str(secondsElapsed), 10, 38, BLACK, 22)

        if secondsElapsed >= 15:
            gameOver = True
            ballList.clear()

    else:
        draw_text(window, "Game Over", screenWidth // 2 - 60, screenHeight // 2 - 20, BLACK)
        draw_text(window, "Final score: " + str(score), screenWidth // 2 - 80, screenHeight // 2 + 10, BLACK)

    pygame.display.update()

pygame.quit()
sys.exit()
 
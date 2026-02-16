# pygame demo 6(b) - Click the Balls Game (15 seconds)

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code

# 2 - Define constants
WHITE = (255, 255, 255)
BLACK = (5, 5, 5)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
GAME_LENGTH = 15  # seconds

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Click the Balls Game")
clock = pygame.time.Clock()

# Font function
def draw_text(surface, text, x, y, color, font_size=24):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# 5 - Initialize variables
ballList = []
score = 0
startTicks = pygame.time.get_ticks()
lastSecond = 0
gameOver = False

# Start with one ball
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
ballList.append(oBall)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

            for oBall in ballList[:]:

        # Try common rectangle names
                if hasattr(oBall, "rect"):
                    hit = oBall.rect.collidepoint(event.pos)
        elif hasattr(oBall, "imageRect"):
            hit = oBall.imageRect.collidepoint(event.pos)
        else:
            continue

        if CONTROLLER_BUTTON_GUIDE:
            ballList.remove(oBall)
            score += 1


    # Calculate elapsed time
    seconds = (pygame.time.get_ticks() - startTicks) // 1000

    # Check if game over
    if seconds >= GAME_LENGTH:
        gameOver = True
        ballList.clear()

    # Add new ball every second
    if not gameOver and seconds > lastSecond:
        lastSecond = seconds
        newBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
        ballList.append(newBall)

    # 8 - Do per-frame actions
    if not gameOver:
        for oBall in ballList:
            oBall.update()

    # 9 - Clear the window
    window.fill(WHITE)

    # 10 - Draw elements
    if not gameOver:
        for oBall in ballList:
            oBall.draw()

        # Draw score and time (BLACK text)
        draw_text(window, f"Score: {score}", 10, 10, BLACK)
        draw_text(window, f"Time: {seconds}", 10, 40, BLACK)
    else:
        draw_text(window, "GAME OVER", WINDOW_WIDTH//2 - 80, WINDOW_HEIGHT//2 - 40, BLACK, 36)
        draw_text(window, f"Final Score: {score}", WINDOW_WIDTH//2 - 90, WINDOW_HEIGHT//2, BLACK, 30)

    # 11 - Update display
    pygame.display.update()

    # 12 - Slow down
    clock.tick(FRAMES_PER_SECOND)

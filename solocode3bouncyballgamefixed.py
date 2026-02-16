import pygame
import random

# -----------------------------
# Helper function to draw text
# -----------------------------
def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# -----------------------------
# Constants
# -----------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# -----------------------------
# Initialize pygame
# -----------------------------
pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bouncy Ball Game")
clock = pygame.time.Clock()

# -----------------------------
# Load assets (use Irv's ball image)
# -----------------------------
ballImage = pygame.image.load("images/ball.png")
ballRect = ballImage.get_rect()

# Success sound (add your own .wav file)
successSound = pygame.mixer.Sound("sounds/boing.wav")

# -----------------------------
# Initial Ball Setup
# -----------------------------
ballRect.x = random.randint(0, WINDOW_WIDTH - ballRect.width)
ballRect.y = random.randint(0, WINDOW_HEIGHT - ballRect.height)

xSpeed = 3
ySpeed = 3

# -----------------------------
# Game Variables
# -----------------------------
score = 0
gameOver = False
startTicks = pygame.time.get_ticks()
endTime = 0

running = True
while running:
    clock.tick(FRAMES_PER_SECOND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mousePos = pygame.mouse.get_pos()

            if ballRect.collidepoint(mousePos):
                score += 1
                successSound.play()

                # Increase speed randomly between 1 and 5
                xIncrease = random.randint(1, 5)
                yIncrease = random.randint(1, 5)

                xSign = 1 if xSpeed > 0 else -1
                ySign = 1 if ySpeed > 0 else -1

                xSpeed = xSign * (abs(xSpeed) + xIncrease)
                ySpeed = ySign * (abs(ySpeed) + yIncrease)

                # Reset ball to random position
                ballRect.x = random.randint(0, WINDOW_WIDTH - ballRect.width)
                ballRect.y = random.randint(0, WINDOW_HEIGHT - ballRect.height)

                # End game at score 5
                if score == 5:
                    gameOver = True
                    endTime = pygame.time.get_ticks()


    if not gameOver:
        ballRect.x += xSpeed
        ballRect.y += ySpeed

      
        if ballRect.left < 0 or ballRect.right > WINDOW_WIDTH:
            xSpeed = -xSpeed

        if ballRect.top < 0 or ballRect.bottom > WINDOW_HEIGHT:
            ySpeed = -ySpeed

   
    window.fill(BLACK)

    if not gameOver:
        window.blit(ballImage, ballRect)

    draw_text(window, f"Score: {score}", 10, 10, WHITE, 30)

    if gameOver:
        totalTime = (endTime - startTicks) / 1000
        draw_text(window, "GAME OVER", 300, 250, WHITE, 50)
        draw_text(window, f"You Won in {totalTime:.2f} seconds!",
                  230, 320, WHITE, 36)

    pygame.display.update()

pygame.quit()

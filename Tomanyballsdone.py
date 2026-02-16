import pygame
import random
from Ball import Ball  # Make sure Ball.py is in the same folder

# Initialize Pygame
pygame.init()

# Set up display
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
self.image = pygame.image.load('ball.png')
pygame.display.set_caption("Click the Balls Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font helper function
def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Game variables
ball_list = []
score = 0
game_time = 15  # seconds
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
last_second = 0
running = True

# Initial ball
ball_list.append(Ball(WIDTH, HEIGHT))

# Main game loop
while running:
    # Fill background
    window.fill(WHITE)
    
    # Calculate elapsed time
    current_ticks = pygame.time.get_ticks()
    elapsed_seconds = (current_ticks - start_ticks) // 1000
    
    # Check for game over
    if elapsed_seconds >= game_time:
        ball_list.clear()
        draw_text(window, f"Game Over! Final Score: {score}", WIDTH//2 - 150, HEIGHT//2, BLACK, 36)
        pygame.display.update()
        pygame.time.delay(3000)  # Show final score for 3 seconds
        break

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for ball in ball_list[:]:
                if ball.is_hit(mouse_pos):
                    ball_list.remove(ball)
                    score += 1

    # Add a new ball every second
    if elapsed_seconds > last_second:
        last_second = elapsed_seconds
        ball_list.append(Ball(WIDTH, HEIGHT))

    # Move and draw balls
    for ball in ball_list:
        ball.move()
        ball.draw(window)

    # Draw score and time
    draw_text(window, f"Score: {score}", 10, 10, BLACK)
    draw_text(window, f"Time: {elapsed_seconds}", 10, 40, BLACK)

    # Update display
    pygame.display.update()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()

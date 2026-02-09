import os
import pygame
import random
from pygame.mixer import Sound


def draw_text(surface, text, x, y, color, font_size=24):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


pygame.init()
pygame.mixer.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Enlightenment Orb")

clock = pygame.time.Clock()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from pygame.mixer import Sound
import os

bounce_sound: Sound = pygame.mixer.Sound(
    os.path.join(BASE_DIR, "sounds", "boing.wav")
)


success_sound: Sound = pygame.mixer.Sound(
    os.path.join(BASE_DIR, "sounds", "boing.wav")
)


BLACK = (10, 10, 30)
PURPLE = (180, 120, 255)
TEAL = (100, 255, 220)
WHITE = (240, 240, 255)


BALL_RADIUS = 30
ball_x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS)
ball_y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS)

x_speed = random.choice([-4, 4])
y_speed = random.choice([-4, 4])

ball_rect = pygame.Rect(
    ball_x - BALL_RADIUS,
    ball_y - BALL_RADIUS,
    BALL_RADIUS * 2,
    BALL_RADIUS * 2
)


score = 0
MAX_SCORE = 5
game_over = False

start_time = pygame.time.get_ticks()
end_time = None


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if ball_rect.collidepoint(event.pos):
                success_sound.play()
                score += 1

                # Reset ball position
                ball_x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS)
                ball_y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS)

                # Increase speed (absolute values)
                x_speed += random.randint(1, 5) * (1 if x_speed > 0 else -1)
                y_speed += random.randint(1, 5) * (1 if y_speed > 0 else -1)

                if score == MAX_SCORE:
                    game_over = True
                    end_time = pygame.time.get_ticks()


    if not game_over:
        ball_x += x_speed
        ball_y += y_speed

        if ball_x <= BALL_RADIUS or ball_x >= WINDOW_WIDTH - BALL_RADIUS:
            x_speed = -x_speed
            bounce_sound.play()

        if ball_y <= BALL_RADIUS or ball_y >= WINDOW_HEIGHT - BALL_RADIUS:
            y_speed = -y_speed
            bounce_sound.play()

        ball_rect.center = (ball_x, ball_y)


    window.fill(BLACK)

    draw_text(window, f"score: {score}", 10, 10, TEAL, 28)

    if not game_over:
        pygame.draw.circle(window, PURPLE, (ball_x, ball_y), BALL_RADIUS)

    if game_over:
        total_time = (end_time - start_time) / 1000
        draw_text(window, "✨ Game Won ✨", 200, 220, WHITE, 48)
        draw_text(
            window,
            f"Time to finish: {total_time:.2f} seconds",
            200,
            280,
            TEAL,
            36
        )

    pygame.display.update()

pygame.quit()
 
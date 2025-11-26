#12-1
# blue_sky.py
import pygame
import sys

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blue Sky")

# Define a blue color
BLUE = (135, 206, 235)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLUE)
    pygame.display.flip()
#12-2
# game_character.py
import pygame
import sys

pygame.init()

class GameCharacter:
    """A character displayed at the center of the screen."""

    def __init__(self, screen):
        self.screen = screen
        # Load bitmap image
        self.image = pygame.image.load('character.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Position the image at the center of the screen
        self.rect.center = self.screen_rect.center

    def draw(self):
        """Draw the character on the screen."""
        self.screen.blit(self.image, self.rect)


# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Character")

# Use the SAME background color as the BMP image’s background
BLUE = (135, 206, 235)

character = GameCharacter(screen)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLUE)
    character.draw()

    pygame.display.flip()
#12-4
import pygame
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Movement")

# Background color
BG_COLOR = (30, 30, 30)


class Rocket:
    """A rocket the player can move around the screen."""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load image
        self.image = pygame.image.load("rocket.bmp")
        self.rect = self.image.get_rect()

        # Start at center of screen
        self.rect.center = self.screen_rect.center

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Move rocket but do not allow leaving the screen."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 3
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 3
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 3
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 3

    def draw(self):
        """Draw rocket on the screen."""
        self.screen.blit(self.image, self.rect)


def run_game():
    rocket = Rocket(screen)

    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # KEYDOWN
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                if event.key == pygame.K_UP:
                    rocket.moving_up = True
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = True

            # KEYUP
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                if event.key == pygame.K_UP:
                    rocket.moving_up = False
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = False

        screen.fill(BG_COLOR)
        rocket.update()
        rocket.draw()
        pygame.display.flip()


run_game()
#12-5
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Key Tester")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print("Key pressed:", event.key)

    screen.fill((0, 0, 0))
    pygame.display.flip()
#12-6
import pygame
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sideways Shooter")

BG_COLOR = (30, 30, 30)


class Ship:
    """A ship that moves up and down on the left side of the screen."""

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load ship image (use your own .bmp file)
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()

        # Start ship on left side, centered vertically
        self.rect.midleft = self.screen_rect.midleft

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Move the ship up or down within screen bounds."""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 4
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 4

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Bullet:
    """A bullet fired by the ship."""

    def __init__(self, screen, ship):
        self.screen = screen
        self.color = (255, 255, 255)
        self.speed = 8

        # Create a small rectangle for the bullet
        self.rect = pygame.Rect(0, 0, 15, 5)
        self.rect.midleft = ship.rect.midright  # Starts at ship’s right side

    def update(self):
        """Move the bullet to the right."""
        self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
    ship = Ship(screen)
    bullets = []

    while True:

        # --- Event Loop ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # KEYDOWN events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    ship.moving_down = True
                if event.key == pygame.K_SPACE:
                    # Fire a bullet
                    bullets.append(Bullet(screen, ship))

            # KEYUP events
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    ship.moving_down = False

        # --- Update Ship ---
        ship.update()

        # --- Update Bullets ---
        for bullet in bullets[:]:
            bullet.update()
            # Remove bullets that move off screen
            if bullet.rect.left > WIDTH:
                bullets.remove(bullet)

        # --- Draw Everything ---
        screen.fill(BG_COLOR)
        ship.draw()
        for bullet in bullets:
            bullet.draw()

        pygame.display.flip()


run_game()

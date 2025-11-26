
def _start_game(self):
    """Start a new game: reset stats, hide mouse, and clear old aliens/bullets."""
    self.stats.reset_stats()
    self.stats.game_active = True

    self.sb.prep_score()
    self.sb.prep_level()
    self.sb.prep_ships()

    self.aliens.empty()
    self.bullets.empty()

    self._create_fleet()
    self.ship.center_ship()

    pygame.mouse.set_visible(False)
def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
        self._start_game()
    if event.key == pygame.K_p:
     if not self.stats.game_active:
        self._start_game()
#14-5
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # Load high score from file
        try:
            with open("high_score.txt", "r") as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0
def _check_high_score(self):
    if self.stats.score > self.stats.high_score:
        self.stats.high_score = self.stats.score
        self.sb.prep_high_score()
if event.type == pygame.QUIT:
    # Save high score before quitting
 with open("high_score.txt", "w") as f:
        f.write(str(self.stats.high_score))
        sys.exit()

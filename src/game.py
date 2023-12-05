import pygame
from random import randint
from duck import Duck
from clock import Clock
from cursor import Cursor

class Game(pygame.sprite.Sprite):
    """
    This class represents the in-game clock used to track the remaining time
    for the Duck Hunt game. It provides methods to start the clock, update the
    countdown, and manage the visual representation of the timer.
    Args: None
    Returns: None
    """
    image = pygame.image.load("Sprites\spawner.png")

    # Scoring
    score = 0
    ducks_hit = 0
    total_shots = 0  # Total Shots Taken
    total_ducks = 0  # Total Ducks Spawned

    # State of Game
    paused = False  # True when game is paused
    over = False  # True when game is over

    # Label for total points
    score_label = pygame.font.Font(None, 25).render("0", True, (255, 255, 255))
    score_rect = score_label.get_rect(left=500, y=428)

    # Label for number of ducks shot
    ducks_shot_label = pygame.font.Font(None, 30).render("0", True, (255, 255, 255))
    ducks_shot_rect = ducks_shot_label.get_rect(x=70, y=418)

    def __init__(self):
        super(Game, self).__init__()

        # Instructions Labels
        self.instructions = pygame.font.Font(None, 35).render(
            "Shoot as many ducks as possible in 1 minute!", True, (255, 255, 255)
        )
        self.instructions_rect = self.instructions.get_rect(x=320, y=100)

        self.instructions2 = pygame.font.Font(None, 35).render(
            "Press \"P\" To Pause", True, (255, 255, 255)
        )
        self.instructions2_rect = self.instructions2.get_rect(x=320, y=140)

        # Paused Game Sprite
        self.paused = pygame.sprite.Sprite()
        self.paused.image = pygame.image.load("Sprites/paused.png")  #change
        self.paused.rect = self.paused.image.get_rect(center=(320, 240))
        self.paused.dx = 0
        self.paused.dy = 0

        # Final Results Labels
        self.results = pygame.font.Font(None, 35).render("", True, (255, 255, 255))
        self.results_rect = self.results.get_rect(x=320, y=100)  # How many ducks were hit
        self.results2 = pygame.font.Font(None, 35).render("", True, (255, 255, 255))
        self.results2_rect = self.results2.get_rect(x=320, y=140)  # Accuracy

        # Counters to delay events
        self.spawn_counter = 0
        self.menu_counter = 0

        self.key_delay = 0
        self.key_delay_start = False

        self.playing = False  # Set to true after instructions go away

        # Create the timer for the game
        self.game_timer = Clock()
        self.game_timer.rect.x = 0
        self.game_timer.rect.y = 0
        self.add(self.game_timer)

    def spawn(self):
        """ Spawn a duck """
        # Generate a random colored duck
        new_duck = Duck(randint(1, 3))

        Game.total_ducks += 1

        self.add(new_duck)

    def update(self):
        # Check if the game time is up
        if Game.over:
            self.menu_counter = 0
            self.playing = False
            Game.over = True

            # Show results
            self.results.value = (
                "You hit " + str(Game.ducks_hit) + " of " + str(Game.total_ducks) + " ducks!"
            )
            self.results2.value = "Accuracy: " + str(
                int((int(Game.ducks_hit) / Game.total_shots) * 100)
            ) + "%"

            self.add(self.results)
            self.add(self.results2)

            self.kill()

    def tick(self):
        if self.playing and not Game.paused and not Game.over:
            # Keep counting until the duck spawner should spawn a new duck
            self.spawn_counter += 1

            if self.spawn_counter >= 75:
                self.spawn()
                self.spawn_counter = 0

        elif not Game.paused and not Game.over:
            # Keep counting until the menu should disappear
            if self.menu_counter >= 250:
                self.remove(self.instructions)
                self.remove(self.instructions2)
                self.menu_counter = 0
                self.playing = True
                self.game_timer.start_clock()

            else:
                self.menu_counter += 1

        elif not Game.paused and not Game.over:
            # Keep the final results until they should disappear
            if self.menu_counter >= 500:
                self.kill()
                exit

            else:
                self.menu_counter += 1

        # Check for the pause button to be pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p] and not Game.over:
            if self.key_delay == 0:
                # Pause or unpause the game
                Game.paused = not Game.paused
                self.key_delay_start = True

                # Display the pause sprite if on pause, remove if not
                if Game.paused:
                    self.add(self.paused)
                    self.add(self.instructions)

                else:
                    # Keep mouse at position it was in when it paused to avoid cheating
                    pygame.mouse.set_pos(Cursor.xPos, Cursor.yPos)

                    # Remove pause label and instructions
                    self.remove(self.paused)
                    self.remove(self.instructions)

        # Advance the keyboard delay
        if self.key_delay_start:
            if self.key_delay > 10:
                self.key_delay = 0
                self.key_delay_start = False

            else:
                self.key_delay += 1

    def update_score(points):
        """ Update The Game Score """
        Game.score += points
        Game.ducks_hit += 1

        Game.score_label = pygame.font.Font(None, 25).render(str(Game.score), True, (255, 255, 255))
        Game.score_rect = Game.score_label.get_rect(left=500, y=428)

        Game.ducks_shot_label = pygame.font.Font(None, 30).render(
            str(Game.ducks_hit), True, (255, 255, 255)
        )
        Game.ducks_shot_rect = Game.ducks_shot_label.get_rect(x=70, y=418)

import pygame

class Clock(pygame.sprite.Sprite):
    """
    This represents the in-game clock used to track the remaining time
    for the Duck Hunt game. It provides methods to start the clock, update the
    countdown, and manage the visual representation of the timer.
    Args: None
    Returns: None
    """
    def __init__(self):
        super(Clock, self).__init__()

        # Timer Display
        self.image = pygame.draw.rect()
        self.rect = self.image.get_rect(topleft=(0, 0))

        self.font = pygame.font.Font(None, 50)
        self.timer = self.font.render("1:00", True, (255, 255, 255))
        self.timer_rect = self.timer.get_rect(topleft=(300, 435))

        # Clock Properties
        self.clock_count = 0
        self.seconds = 60

       

        self.started = False

    # Start the clock
    def start_clock(self):
        self.started = True

    def update(self):
        # Check if clock has run out of time
        if self.seconds <= 0:
            self.started = False
            #set loop to endloop here
            pygame.mouse.set_visible(True)  # Show 
            return False

        # Change the clock's color to red when it gets down to the last minute
        if self.seconds <= 10:
            self.timer = self.font.render("0:" + str(self.seconds).rjust(2, "0"), True, (255, 0, 0))

    # Update the Clock's Label
    def update_clock(self):
        label = "0:" + str(self.seconds).rjust(2, "0")


        # Update The Clock's Label
        self.timer = self.font.render(label, True, (255, 255, 255))

    # Perform the Clock countdown
    def countdown(self):
        # Only Do Countdown if not paused and playing the game
        if self.clock_count >= 100:
            self.seconds -= 1

            # Show the new time on the clock
            self.update_clock()

            self.clock_count = 1

        else:
            self.clock_count += 1

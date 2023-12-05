import pygame
from random import randint
from game import Game

class Duck(pygame.sprite.Sprite):
    """ Duck Class """
    def __init__(self, duckType):
        super(Duck, self).__init__()

        # Colors Available
        colors = ["", "black", "blue", "red"]
        duckColor = colors[duckType]

        # Sprites for the Duck
        self.flyRight = [
            pygame.image.load(f"Sprites/{duckColor}/duck1.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck2.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck3.png")
        ]

        self.flyStraightRight = [
            pygame.image.load(f"Sprites/{duckColor}/duck4.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck5.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck6.png")
        ]

        self.flyLeft = [
            pygame.image.load(f"Sprites/{duckColor}/duck7.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck8.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck9.png")
        ]

        self.flyStraightLeft = [
            pygame.image.load(f"Sprites/{duckColor}/duck10.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck11.png"),
            pygame.image.load(f"Sprites/{duckColor}/duck12.png")
        ]

        self.die = [
            pygame.image.load(f"Sprites/{duckColor}/duckDie1.png"),
            pygame.image.load(f"Sprites/{duckColor}/duckDie2.png"),
            pygame.image.load(f"Sprites/{duckColor}/duckDie3.png")
        ]

        # Intialize Duck Sprite At Random X-Location
        self.image = self.flyRight[0]
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 470)
        self.rect.y = 350
        self.dx = 0
        self.dy = -1

        # Point Values Based On Duck Color
        pointValues = {"blue": 25, "red": 50, "black": 75}

        # Direction Constants
        self.RIGHT = 1
        self.LEFT = 2

        # Duck Variables
        self.alive = True
        self.direction = randint(1, 2)
        self.straight = False  # True if duck is flying straight
        self.points = pointValues[duckColor]

        # Animation Frames
        self.frames = [
            self.flyRight[1], self.flyRight[2], self.flyRight[1],
            self.flyRight[0]
        ]

        # Points above the duck's head when it's shot
        self.deathScore = pygame.font.SysFont(None, 25).render(
            str(self.points), True, (255, 255, 255)
        )
        self.deathScore_rect = self.deathScore.get_rect()
        self.deathScore_rect.x = self.rect.x
        self.deathScore_rect.y = self.rect.top - 5

        # Animation Variables
        self.dieDelay = 0  # Delay Duck Falling
        self.continueDeath = False
        self.animationCount = 0
        self.frame = 0  # What frame of the animation?
        self.directionCount = 0

        # Set velocity based on direction
        if self.direction == self.RIGHT:
            self.dx = 0.5
        else:
            self.dx = -0.5

    def change_direction(self):
        """ Decide to change duck's direction """
        randomNum = randint(1, 340)

        if randomNum % 5 == 0:
            # Switch the duck's direction
            if self.direction == self.RIGHT:
                self.direction = self.LEFT
                self.dx = -0.5
            else:
                self.direction = self.RIGHT
                self.dx = 0.5

        # Decide if it will fly straight or not
        randomNum = randint(1, 340)

        if randomNum % 5 == 0:
            # Change duck to straight or up
            self.straight = not self.straight

    def update(self):
        """ Update the sprite """
        if not Game.paused and not Game.over:
            # Check if the duck is alive
            if self.alive:
                # Duck is alive
                if (
                    self.rect.bottom < 0
                    or self.rect.right < 0
                    or self.rect.left > 640
                ):
                    # Duck is off the screen, destroy
                    self.kill()

                # Check if the duck should try and change directions
                if self.directionCount < 100:
                    self.directionCount += 1
                else:
                    self.change_direction()
                    self.directionCount = 0

                # Check if the duck is going straight and change velocity
                if self.straight:
                    self.dy = 0

                    if self.direction == self.RIGHT:
                        self.dx = 1
                    else:
                        self.dx = -1
                else:
                    # Duck is flying upwards
                    self.dy = -1

                # Update the animation frames based on duck's velocity
                if not self.alive:
                    self.frames = [self.die[1], self.die[2]]
                elif self.direction == self.RIGHT:
                    if self.straight:
                        self.frames = [
                            self.flyStraightRight[1],
                            self.flyStraightRight[2],
                            self.flyStraightRight[1],
                            self.flyStraightRight[0],
                        ]
                    else:
                        self.frames = [
                            self.flyRight[1],
                            self.flyRight[2],
                            self.flyRight[1],
                            self.flyRight[0],
                        ]
                elif self.direction == self.LEFT:
                    if self.straight:
                        self.frames = [
                            self.flyStraightLeft[1],
                            self.flyStraightLeft[2],
                            self.flyStraightLeft[1],
                            self.flyStraightLeft[0],
                        ]
                    else:
                        self.frames = [
                            self.flyLeft[1],
                            self.flyLeft[2],
                            self.flyLeft[1],
                            self.flyLeft[0],
                        ]

                if self.frame >= len(self.frames):
                    self.frame = 0

                # Check for mouse clicks
                if Cursor.clicked:
                    # Prevent the shooting of a duck that's behind the tree
                    if not (150 < Cursor.xPos < 240) or not (220 < Cursor.yPos < 390):
                        # Check if the mouse was over the duck
                        if (
                            self.rect.left <= Cursor.xPos <= self.rect.right
                            and self.rect.top <= Cursor.yPos <= self.rect.bottom
                        ):
                            # Duck was shot - Kill it
                            self.shot()
            else:
                # Duck is Dead, Destroy once it hits the ground
                if self.rect.bottom > 370:
                    self.kill()

    def shot(self):
        """ Kill the duck """
        Game.update_score(self.points)

        self.alive = False  # Set the duck to dead
        self.image = self.die[0]  # Replace with starting death animation

        self.frame = 0
        self.animationCount = 0

        # Freeze the duck
        self.dx = 0
        self.dy = 0

        # Display score above duck's head
        self.deathScore_rect.x = self.rect.x
        self.deathScore_rect.y = self.rect.top - 10
        games.screen.blit(self.deathScore, self.deathScore_rect)

    def update_animation(self):
        self.animationCount += 1

        if self.animationCount >= 17:
            # Change animation for falling dead duck
            if not self.alive:
                if self.continueDeath:
                    self.dy = 2

                    # Advance the Death Animation
                    frames = [self.die[2], self.die[1]]

                    self.image = frames[self.frame]

                    self.frame += 1

                    # Make Sure the frame stays within the correct range
                    if self.frame >= len(frames):
                        self.frame = 0
            # Change animation for duck that's not dead
            else:
                if self.frame >= len(self.frames):
                    self.frame = 0

                self.image = self.frames[self.frame]

                self.frame += 1

                if self.frame >= len(self.frames):
                    self.frame = 0

            # Reset the animation counter
            self.animationCount = 0

    def tick(self):
        """ Tick Method """
        # Tick only if game is not paused
        if not Game.paused:
            if not self.alive:
                # This will display the point value above the head and when it's done the duck will start to fall
                if self.dieDelay > 50 and not self.continueDeath:
                    self.dy = 1

                    self.continueDeath = True
                    self.frame = 0

                elif not self.continueDeath:
                    self.dieDelay += 1
            # This elif will help birds continue to fly
            # At the correct angle and direction after resuming from a pause
            elif (self.dx == 0) and (self.dy == -1):
                if not self.straight:
                    if self.direction == self.RIGHT:
                        self.dx = 0.5
                    else:
                        self.dx = -0.5
            # Update the Duck's animation
            self.update_animation()
        elif Game.paused:
            # Game is Paused - Freeze the duck
            self.dx = 0
            self.dy = 0

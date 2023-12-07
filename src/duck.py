import pygame
from random import randint
from cursor import Cursor

class Duck(pygame.sprite.Sprite):
    """
    This represents a duck in the Duck Hunt game. 
    It handles the duck's movement, animation, and response to being shot.
    Args: None
    Returns: None
    """
    def __init__(self):
        super(Duck, self).__init__()

        # Sprites for the Duck
        self.flyRight = [
            pygame.image.load(f"assets/njit"),
            pygame.image.load(f"assets/ualbany"),
            pygame.image.load(f"assets/ualbany"),
        ]

        self.flyStraightRight = [
            pygame.image.load(f"assets/njit"),
            pygame.image.load(f"assets/ualbany"),
            pygame.image.load(f"assets/ualbany"),
        ]

        self.flyLeft = [
            pygame.image.load(f"assets/njit"),
            pygame.image.load(f"assets/ualbany"),
            pygame.image.load(f"assets/ualbany"),
        ]

        self.flyStraightLeft = [
            pygame.image.load(f"assets/njit"),
            pygame.image.load(f"assets/ualbany"),
            pygame.image.load(f"assets/ualbany"),
        ]

        self.die = [
            pygame.image.load(f"assets/njit"),
            pygame.image.load(f"assets/ualbany"),
            pygame.image.load(f"assets/ualbany"),
        ]

        # Intialize Sprite At Random X-Location
        self.image = self.flyRight[0]
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 470)
        self.rect.y = 350
        self.dx = 0
        self.dy = -1

        
        # Direction Constants
        self.RIGHT = 1
        self.LEFT = 2

        # Duck Variables
        self.alive = True
        self.direction = randint(1, 2)
        self.straight = False  # True if duck is flying straight
        self.points = 10


        # Set velocity based on direction
        if self.direction == self.RIGHT:
            self.dx = 0.5
        else:
            self.dx = -0.5

    def change_direction(self):
        """ Decide to change sprite's direction """
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
        if not Cursor.clicked:
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
        """ Kill the sprite """
        # Pass the update_score function as a callback
        self.callback(self.points)  #adds points

        self.alive = False  # Set the duck to dead
        self.image = self.die[0]  #Replaces image, might do large X over mascots eyes

        self.frame = 0
        self.animationCount = 0

        # Freeze the duck
        self.dx = 0
        self.dy = 0


    

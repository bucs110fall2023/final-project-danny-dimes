import pygame
from random import randint


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
        spriteChooser = randint(0,1)
        
        self.ualbany = pygame.image.load(f"assets/ualbany.png")
        self.njit = pygame.image.load(f"assets/njit.png")
        if spriteChooser == 0:
            self.image = self.ualbany
            self.image = pygame.transform.scale(self.image, (150,150))
        if spriteChooser == 1:
            self.image = self.njit
        # Intialize Sprite At Random X-Location
        
        self.rect = pygame.Rect(self.image.get_rect().left + 40, self.image.get_rect().top, 40, self.image.get_rect().height)
        self.rect.x = randint(10, 1000)
        self.rect.y = 350
        self.speed = 5
        self.directionCount=0
        


        # Direction Constants
        self.RIGHT = 1
        self.LEFT = 2

        # Duck Variables
        self.alive = True
        self.direction = randint(1, 2)
        self.straight = False  # True if duck is flying straight
        self.points = 10


    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed



    def change_direction(self):
        """ Decide to change sprite's direction """
        randomNum = randint(1, 340)

        if randomNum % 5 == 0:
            # Switch the duck's direction
            if self.direction == self.RIGHT:
                self.direction = self.LEFT
                self.move_left()
            else:
                self.direction = self.RIGHT
                self.move_right()

        # Decide if it will fly straight or not
        randomNum = randint(1, 400)

        if randomNum % 5 == 0:
            # Change duck to straight or up
            self.straight = not self.straight


    def update(self):
        """ Update the sprite """
        #Check if the duck is alive
        
    
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
            if self.direction == self.RIGHT:
                self.move_right()
            else:
                self.move_left()
        else:
            # Duck is flying upwards
            self.move_up()
            self.change_direction()
           
       



    

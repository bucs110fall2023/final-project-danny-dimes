import pygame
from random import randint


class Mascot(pygame.sprite.Sprite):
    """
    Desc: Initializes a mascot sprite with random image selection and movement behavior.
    Args: None
    Returns: None
    """
    def __init__(self):
        super(Mascot, self).__init__()

        # Sprites for the mascot
        spriteChooser = randint(0,6)
        
        self.ualbany = pygame.image.load(f"assets/ualbany.png")
        self.njit = pygame.image.load(f"assets/njit.png")
        self.umass = pygame.image.load(f"assets/umass.png")
        self.umaine = pygame.image.load(f"assets/umaine.png")
        self.umbc = pygame.image.load(f"assets/umbc.png")
        self.unh = pygame.image.load(f"assets/unh.png")
        self.bryant = pygame.image.load(f"assets/bryant.png")
        if spriteChooser == 0:
            self.image = self.ualbany
            self.image = pygame.transform.scale(self.image, (150,150))
        elif spriteChooser == 1:
            self.image = self.njit
            self.image = pygame.transform.scale(self.image, (150,150))
        elif spriteChooser == 2:
            self.image = self.umaine
            self.image = pygame.transform.scale(self.image, (150,150))
        elif spriteChooser == 3:
            self.image = self.umass
            self.image = pygame.transform.scale(self.image, (150,150))
        elif spriteChooser == 4:
            self.image = self.umbc
            self.image = pygame.transform.scale(self.image, (150,150))
        elif spriteChooser == 5:
            self.image = self.unh
            self.image = pygame.transform.scale(self.image, (150,150))
        elif spriteChooser == 6:
            self.image = self.bryant
            self.image = pygame.transform.scale(self.image, (150,150))
        #sprite 
        self.rect = pygame.Rect(self.image.get_rect().left + 100, self.image.get_rect().top, 100, self.image.get_rect().height+50)

        #spawn sprite at location
        self.leftOrRight=randint(0,10)
        if self.leftOrRight%2==0:
            self.rect.x = 10
        else:
            self.rect.x=1500
        self.rect.y = randint(100,400)
        self.speed = 5
        self.directionCount=0

        # Direction Constants
        self.RIGHT = 1
        self.LEFT = 2

        # mascot Variables
        self.alive = True
        self.direction = randint(1, 2)
        self.straight = False  # True if mascot is flying straight
        self.points = 10


    def move_up(self):
        """ Move sprite up by increment """
        self.rect.y -= self.speed

    def move_down(self):
        """ Move sprite down by increment """
        self.rect.y += self.speed

    def move_right(self):
        """ Move sprite right by increment """
        self.rect.x += self.speed

    def move_left(self):
        """ Move sprite left by increment """
        self.rect.x -= self.speed



    def change_direction(self):
        """ Decide to change sprite's direction """
        randomNum = randint(1, 200)

        if randomNum % 5 == 0:
            # Switch the mascot's direction
            if self.direction == self.RIGHT:
                self.direction = self.LEFT
                self.move_left()
            else:
                self.direction = self.RIGHT
                self.move_right()

        # Decide if it will fly straight or not
        randomNum = randint(1, 400)

        if randomNum % 5 == 0:
            # Change mascot to straight or up
            self.straight = not self.straight

    def update(self):
        """ Update the sprite """
        # Check if the mascot should try and change directions
        if self.directionCount < 100:
            self.directionCount += 1
        else:
            self.change_direction()
            self.directionCount = 0

        # Check if the mascot is going straight and change velocity
        if self.straight:
            if self.direction == self.RIGHT:
                self.move_right()
            else:
                self.move_left()
        else:
            # mascot is flying upwards
            self.move_up()
            self.change_direction()
        if (self.rect.bottom < 0):
            self.move_up()
        elif (self.rect.left < 0):
            self.direction=self.RIGHT
            
        elif (self.rect.right > 1500):
            self.direction=self.LEFT

       



    

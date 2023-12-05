import pygame
from game import Game

class Cursor(pygame.sprite.Sprite):
    """ Cursor Object """
    clicked = False
    
    xPos = pygame.mouse.get_pos()[0]
    yPos = pygame.mouse.get_pos()[1]
    
    def __init__(self):
        """ Cursor Initializer """
        super(Cursor, self).__init__()
        
        # Load image and rect attributes
        self.image = pygame.image.load("Sprites/cursor.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (Cursor.xPos, Cursor.yPos)
        
        self.mouseClicked = False
        self.mouseCounter = 0

        # Load gunshot sound
        self.gunShotSound = pygame.mixer.Sound("Sounds/shot.wav")
        
    def update(self):
        # Keep the sprite at the same x and y location as the mouse
        self.rect.topleft = (Cursor.xPos, Cursor.yPos)

    def tick(self):
        """ Check For Mouse Click """
        if not Game.paused and not Game.over:
            # Check if the mouse was clicked
            if pygame.mouse.get_pressed()[0] and not Cursor.clicked:
                # Play Gunshot Sound and add Total Sounds
                Cursor.clicked = True
                self.gunShotSound.play()
                Game.totalShots += 1
            
            # Avoid repeated mouse clicks 
            if Cursor.clicked:
                if self.mouseCounter > 10 and not pygame.mouse.get_pressed()[0]:
                    Cursor.clicked = False
                    self.mouseCounter = 0

                else:
                    self.mouseCounter += 1

            # Update cursor position
            Cursor.xPos, Cursor.yPos = pygame.mouse.get_pos()

            # Bring the tree and grass in front of all the ducks
            self.foreground.elevate()

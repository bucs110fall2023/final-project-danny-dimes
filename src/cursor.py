import pygame
from livewires import games, colour

class Cursor(games.Sprite):
    """ Cursor Object """
    clicked = False
    
    xPos = games.mouse.x
    yPos = games.mouse.y
    
    def __init__(self):
        """ Cursor Initializer """
        super(Cursor, self).__init__(image=games.load_image("Sprites/cursor.png"), x=games.mouse.x, y=games.mouse.y)
        
        self.mouseClicked = False
        self.mouseCounter = 0

        # Load gunshot sound
        self.gunShotSound = games.load_sound("Sounds/shot.wav")
        
    def update(self):
        # Keep the sprite at the same x and y location as the mouse
        self.x = Cursor.xPos
        self.y = Cursor.yPos

        # Remove and readd to put on top of any birds
        games.screen.remove(self)
        games.screen.add(self)
        
    def tick(self):
        """ Check For Mouse Click """
        if not Game.paused and not Game.over:
            # Check if the mouse was clicked
            if games.mouse.is_pressed(0) and not Cursor.clicked:
                # Play Gunshot Sound and add Total Sounds
                Cursor.clicked = True
                self.gunShotSound.play()
                Game.totalShots += 1
            
            # Avoid repeated mouse clicks 
            if Cursor.clicked:
                if self.mouseCounter > 10 and not games.mouse.is_pressed(0):
                    Cursor.clicked = False
                    self.mouseCounter = 0

                else:
                    self.mouseCounter += 1

            # Update cursor position
            Cursor.xPos = games.mouse.x
            Cursor.yPos = games.mouse.y

            # Bring the tree and grass infront of all the ducks
            foreground.elevate()
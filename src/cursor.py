import pygame

class Cursor(pygame.sprite.Sprite):
    """
    This class represents the cursor used in the Duck Hunt game. It is responsible
    for tracking the mouse position and detecting mouse clicks
    The cursor sprite is updated to follow the mouse movements.
    Args: None
    Returns: None
    """
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

    
        
    def update(self):
        # Keep the sprite at the same x and y location as the mouse
        self.rect.topleft = (Cursor.xPos, Cursor.yPos)

    def tick(self, is_paused, is_over, total_shots, elevate_foreground):
        """ Check For Mouse Click """
        if not is_paused and not is_over:
            # Check if the mouse was clicked
            if pygame.mouse.get_pressed()[0] and not Cursor.clicked:
                
                Cursor.clicked = True
              
                total_shots += 1
            
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
            elevate_foreground()

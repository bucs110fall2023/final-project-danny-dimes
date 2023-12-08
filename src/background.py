import pygame

class Background(pygame.sprite.Sprite):
    """
    Desc: Initializes the game's background with a specified image file and location.
    Args:
    - image_file (str): Path to the image file for the background (default: 'assets/background.png')
    - location (list): Coordinates specifying the top-left corner position of the background (default: [0, 0])
    Returns: None
    """
    def __init__(self, image_file= 'assets/background.png', location=[0,0]):
        super().__init__()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = pygame.display.get_window_size()
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

 
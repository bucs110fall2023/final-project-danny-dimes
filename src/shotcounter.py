import pygame

class shotcounter(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, width=175, height=75, image_file="assets/button.png", text="Press Me"):
        super().__init__()
        self.image = pygame.image.load(image_file)

        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        
        self.color = "white"
        self.message = pygame.font.SysFont(None, 14).render(text, True, self.color)
        self.image.blit(self.message, (self.rect.width/2, self.rect.height/2))
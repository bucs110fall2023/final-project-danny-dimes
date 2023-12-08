import pygame

class Scoreboard(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, width=175, height=75, color=(200, 0, 200), text="0"):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.color = color
        self.image.fill(self.color)
        self.message = pygame.font.SysFont(None, 36).render(text, True, "white")
        self.image.blit(self.message, (20, 20)) #change cords
        self.image.blit("Score:", (x,y)) #replace x/y
    def update(self,totalPoints):
        self.message = pygame.font.SysFont(None, 36).render(str(totalPoints), True, "white")
        self.image.blit(self.message, (20, 20)) #change cords
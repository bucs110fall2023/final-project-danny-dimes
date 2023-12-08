import pygame

class Scoreboard(pygame.sprite.Sprite):
    """
    This represents a mascot in the Duck Hunt game. 
    It handles the mascot's movement, animation, and response to being shot.
    Args: None
    Returns: None
    """
    def __init__(self, x=10, y=10, width=200, height=50, color=(0, 0, 0)):
        super().__init__()
        self.font = pygame.font.SysFont(None, 36)
        self.text_color = (255, 255, 255)
        self.score = 0
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_score(self, new_score):
        self.score = new_score
        text = f"Score: {self.score}"
        rendered_text = self.font.render(text, True, self.text_color)
        self.image.fill((0, 0, 0))  # Clear previous score
        self.image.blit(rendered_text, (10, 10))  # Adjust position as needed

import pygame 
from src.duck import Duck
from src.clock import Clock
from src.scoreboard import Scoreboard
from src.background import Background

class Controller:
  
  def __init__(self):
      pygame.init()
      pygame.font.init()
      #set background
      self.screen = pygame.display.set_mode()
      self.background = Background()
      self.screen.blit(self.background.image, self.background.rect)
      self.fps = 60
      self.timer = pygame.time.Clock()
      self.mascots = pygame.sprite.Group()
      self.num_mascots=5



      self.font = pygame.font.SysFont(None, 50)
      self.timer=self.font.render("1:00", True, "white")
      self.screen.blit(self.timer, (100,100))
      


      
    
      self.clock = Clock
      self.scoreboard = Scoreboard
      
      self.all_sprites = pygame.sprite.Group()
      
      self.all_sprites.add(self.background)
      self.all_sprites.add(self.mascots)
      for _ in range (self.num_mascots):
        self.mascots.add(Duck())

      self.state="GAME"

    #Score variables
      self.score=0
      self.total_shots=0
      self.ducks_hit=0
      self.total_ducks = self.num_mascots

  def mainloop(self):
    while True:
      if self.state == "GAME":
        self.gameloop()
        self.clock.start_clock
      elif self.state == "PAUSE":
        self.pauseloop()  
      elif self.state =="END":
        self.endloop()

  def gameloop(self): #actual game goes here
    while True:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          for s in self.mascots:
            if s.rect.collidepoint(event.pos):
              s.kill()
              self.ducks_hit+=1
              self.score+=100
              self.total_ducks-=1
              self.mascots.add(Duck())
              print("clicked")
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.state = "END" 
          

      self.clock.update_clock
      if self.clock.update_clock == False: #if time = 0, go to endloop
        self.state=="END"
      
        
      for s in self.mascots:
        s.update() #update mascots
      # self.scoreboard.update(self,self.score)#point variable inside
      

      #redraw models
      self.all_sprites.draw(self.screen)
      #redraw background
      # self.screen.fill((255, 255, 255))  # Fill the screen with white
      # self.screen.blit(self.background.image, self.background.rect)
      self.mascots.draw(self.screen)  # Draw the mascots on the screen
      #self.screen.blit(self.instructions, self.instructions_rect)
      #self.screen.blit(self.instructions2, self.instructions2_rect)
      pygame.display.flip()
      
      

  def pauseloop(self):
    # Handle events specific to the "PAUSE" state
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.state = "END"
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          self.state = "GAME"  # Resume the game

        # Render the pause screen
    self.screen.fill((255, 255, 255))  # Fill the screen with white
    self.screen.blit(self.instructions, self.instructions_rect)
    self.screen.blit(self.instructions2, self.instructions2_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Paused", True, (255, 0, 0))
    text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
    self.screen.blit(text, text_rect)
    pygame.display.flip()

  def endloop(self):
    pygame.quit()
    exit()

if __name__ == "__main__":
    duck_hunt_controller = Controller()  # Updated class name
    duck_hunt_controller.mainloop()  # Updated method name

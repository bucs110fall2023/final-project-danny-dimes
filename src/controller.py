import pygame 
from src.duck import Duck
from src.clock import Clock
from src.scoreboard import Scoreboard
from src.shotcounter import Shotcounter

from src.background import Background

class Controller:
  
  def __init__(self):
      pygame.init()
      #set background
      self.screen = pygame.display.set_mode()
      self.background = Background()
      self.screen.blit(self.background.image, self.background.rect)
      self.fps = 60
      self.timer = pygame.time.Clock()
      self.mascots = pygame.sprite.Group()
      num_mascots=3
      #possibly add interval for adding (i.e spawns every 5 seconds)
      for _ in range (num_mascots):
        self.mascots.add(Duck())
    
      self.clock = Clock
      self.scoreboard = Scoreboard
      self.shotcounter = Shotcounter
      
      

      self.state="GAME"

    #Score variables
      self.score=0
      self.total_shots=0
      self.ducks_hit=0
  
     

      # Instructions Labels
      # self.instructions = pygame.font.Font(None, 35).render(
      #     "Shoot as many ducks as possible in 1 minute!", True, (255, 255, 255)
      # )
      # self.instructions_rect = self.instructions.get_rect(x=320, y=100)

      # self.instructions2 = pygame.font.Font(None, 35).render(
      #     "Press \"P\" To Pause", True, (255, 255, 255)
      # )
      # self.instructions2_rect = self.instructions2.get_rect(x=320, y=140)

      # # Paused Game Sprite
      # self.paused = pygame.sprite.Sprite()
      # #self.paused.image = pygame.image.load("assets/paused.png")  #change
      # self.paused.rect = self.paused.image.get_rect(center=(320, 240))
      # self.paused.dx = 0
      # self.paused.dy = 0
      
 
      
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
              s.kill
              self.ducks_hit+=1
              self.score+=100

          self.total_shots+=1
      
      
      self.clock.update_clock
      if self.clock.update_clock == False: #if time = 0, go to endloop
        self.state=="END"
      
        
      self.mascots.update #update mascots
      # self.scoreboard.update(self,self.score)#point variable inside
      

      #redraw models
      #redraw background
      self.screen.fill((255, 255, 255))  # Fill the screen with white
      self.screen.blit(self.background.image, self.background.rect)
      self.mascots.draw(self.screen)  # Draw the mascots on the screen
      #self.screen.blit(self.instructions, self.instructions_rect)
      #self.screen.blit(self.instructions2, self.instructions2_rect)
      pygame.display.flip()
            
      # Update game objects
      self.timer.tick(self.fps)

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

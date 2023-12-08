import pygame 
from src.mascot import Mascot
from src.scoreboard import Scoreboard
from src.background import Background

class Controller:
  
  def __init__(self):
      pygame.init()
      pygame.font.init()
      #set background
      
      self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
      self.width, self.height = pygame.display.get_window_size()
      self.background = Background()
      self.screen.blit(self.background.image, self.background.rect)
      self.fps = 60
      self.mascots = pygame.sprite.Group()
      self.num_mascots=5


      #setting up timer
      self.font = pygame.font.SysFont(None, 50)
      self.timerSecs = 60
      self.timerDisplay=self.font.render("1:00", True, "white")
      self.timer = pygame.USEREVENT                                                
      pygame.time.set_timer(self.timer, 1000)    

      self.scoreboard = Scoreboard
      
      self.all_sprites = pygame.sprite.Group()
      
      self.all_sprites.add(self.background)
      self.all_sprites.add(self.mascots)
      for _ in range (self.num_mascots):
        self.mascots.add(Mascot())

      self.state="GAME"

    #Score variables
      self.score=0
      self.total_shots=0
      self.mascots_hit=0
      self.total_mascots = self.num_mascots

  def mainloop(self):
    while True:
      if self.state == "GAME":
        self.gameloop()
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
        if event.type==self.timer:
          if self.timerSecs>0:
            self.timerSecs-=1
            print("0:" + str(self.timerSecs).rjust(2, "0"))
            self.timerDisplay = self.font.render( "0:" + str(self.timerSecs).rjust(2, "0"),True,"white")
          else:
            pygame.time.set_timer(self.timer, 0)    
            self.state="END"
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
          for s in self.mascots:
            if s.rect.collidepoint(event.pos):
              s.kill()
              self.mascots_hit+=1
              self.score+=100
              self.total_mascots-=1
              self.mascots.add(Mascot())
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.state = "END" 
            return
          elif event.key == pygame.K_p:
            
            self.state="PAUSE"
            return

      for s in self.mascots:
        s.update() #update mascots


      # self.scoreboard.update(self.score)#point variable inside
      

      #redraw models
      self.all_sprites.draw(self.screen)
      #redraw scoreboard
      #self.screen.blit(self.scoreboard.image, self.scoreboard.rect)

      self.mascots.draw(self.screen)  # Draw the mascots on the screen
      self.screen.blit(self.timerDisplay, (self.width // 2, self.height // 1.07))
      
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
    font = pygame.font.Font(None, 36)
    text = font.render("Paused", True, "black")
    text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
    self.screen.blit(text, text_rect)
    pygame.display.flip()

  def endloop(self):
    pygame.quit()
    exit()


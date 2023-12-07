import pygame 

class Controller:
  
  def __init__(self):
      pygame.init()
      self.fps = 60
      self.timer = pygame.time.Clock()
      
  def mainloop(self):
    while True:
      if self.state == "GAME":
        self.gameloop()
      elif self.state == "PAUSE":
        self.pauseloop()  
      elif self.state =="END":
        self.endloop()


  def pauseloop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.state = "END"
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          self.state = "GAME"  # Resume the game
        # Handle other pause menu events

  def endloop(self):
    pygame.quit()
    exit()

  def gameloop(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
              
        #elif event.type == pygame.KEYDOWN:
          #if event.key == pygame.K_p:
            #controller.state = "PAUSE"  # Pause game
              #return  # Exit the gameloop, as the game is paused
            
      # Update game objects
      self.timer.tick(self.fps)
   
    self.mascots = pygame.sprite.Group()
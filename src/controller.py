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
        self.game.run_game = False
      # handle other menu events

    # update data for the menu
    self.game.menu_manager.update()

    # redraw the menu
    self.game.menu_manager.draw()

  def gameloop(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
              # handle other game events

   
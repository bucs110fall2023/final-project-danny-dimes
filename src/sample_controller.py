import pygame 

class Controller:
  
  def __init__(self):
      pygame.init()
      self.fps = 60
      self.timer = pygame.time.Clock()
      self.game = DuckHuntingGame()

  def mainloop(self):
    while self.game.run_game:
      self.timer.tick(self.fps)
      if self.game.state == "menu":
        self.menuloop()
      elif self.game.state == "game":
        self.gameloop()
      elif self.game.state == "game_over":
        self.gameoverloop()

  def menuloop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game.run_game = False
      # handle other menu events

    # update data for the menu
    self.game.menu_manager.update()

    # redraw the menu
    self.game.menu_manager.draw()

  def gameloop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          self.game.run_game = False
            # handle other game events

    # update game data
    self.game.level_manager.update()
    self.game.ui_manager.update()

    # redraw the game
    self.game.level_manager.draw()
    self.game.ui_manager.draw()

  def gameoverloop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game.run_game = False
      # handle other game over events

    # update data for the game over screen
    self.game.menu_manager.update()

    # redraw the game over screen
    self.game.menu_manager.draw()


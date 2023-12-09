import pygame 
from src.mascot import Mascot
from src.background import Background

class Controller:
  """
  Desc: Initializes and manages the game environment, 
  handles events, and controls the game state transitions.
  Args: none
  Returns: none
  """
  def __init__(self):
      pygame.init()
      pygame.font.init()
      #set background
      
      self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
      self.width, self.height = pygame.display.get_window_size()
      self.background = Background()
      self.screen.blit(self.background.image, self.background.rect)
      self.mascots = pygame.sprite.Group()
      self.num_mascots=5


      #setting up timer
      self.font = pygame.font.SysFont(None, 100)
      self.timer_secs = 60
      self.timer_display=self.font.render("1:00", True, "white")
      self.timer = pygame.USEREVENT                                                
      pygame.time.set_timer(self.timer, 1000)    



    #setting up scoreboard
      self.font_one = pygame.font.SysFont(None, 60)
      self.scoreboard_display= self.font_one.render("Score: 0", True, "white")

      
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
    "Runs certain loop depending on game conditions"
    while True:
      if self.state == "GAME":
        self.gameloop()
      elif self.state == "PAUSE":
        self.pauseloop()  
      elif self.state =="END":
        self.endloop()

  def gameloop(self):
    "Handles game being played"
    while True:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==self.timer:
          if self.timer_secs>0:
            self.timer_secs-=1
            self.timer_display = self.font.render( "0:" + str(self.timer_secs).rjust(2, "0"),True,"white")
          else:
            pygame.time.set_timer(self.timer, 0) 
              
            self.state="END"
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
          for s in self.mascots:
            if s.rect.collidepoint(event.pos):
              s.kill()
              self.total_shots+=1
              self.mascots_hit+=1
              self.score+=100
              self.total_mascots-=1
              self.mascots.add(Mascot())
              self.scoreboard_display= self.font_one.render("Score: " + str(self.score), True, "white")
            else:
              self.total_shots+=1
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.state = "END" 
            return
          elif event.key == pygame.K_p:
            self.state="PAUSE"
            return

      for s in self.mascots:
        s.update() #update mascots
      #redraw models
      self.all_sprites.draw(self.screen)
      #redraw scoreboard
      self.screen.blit(self.scoreboard_display, (self.width // 1.25, self.height // 1.09))

      self.mascots.draw(self.screen)  # Draw the mascots on the screen
      self.screen.blit(self.timer_display, (self.width // 2.1, self.height // 1.09))
      
      pygame.display.flip()
  def pauseloop(self):
    "Handles what happens when game is paused"
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.state = "END"
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
          self.state = "GAME"  # Resume the game

        # Render the pause screen
    self.screen.fill((255, 255, 255))
    pause_font = pygame.font.Font(None, 100 )
    text = pause_font.render("Game Paused", True, "black")
    text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
    self.screen.blit(text, text_rect)
    pygame.display.flip()

  def endloop(self):
    "handles end game screen"
    self.all_sprites.draw(self.screen)
    self.screen.blit(self.timer_display, (self.width // 2.1, self.height // 1.09))
    self.screen.blit(self.scoreboard_display, (self.width // 1.25, self.height // 1.09))
    for s in self.mascots:
      s.kill() 
    
    accuracy= round(self.mascots_hit/self.total_shots*100, 2)
    pauseFont = pygame.font.Font(None, 50 )
    textOne = pauseFont.render("Game Over!", True, "white")
    textOne_rect = textOne.get_rect(center=(self.width // 2, self.height // 3))
    self.screen.blit(textOne, textOne_rect)

    textTwo = pauseFont.render("You hit a total of " + str(self.mascots_hit) + " mascots of rival schools!", True, "white")
    textTwo_rect = textTwo.get_rect(center=(self.width // 2, self.height // 2.6))
    self.screen.blit(textTwo, textTwo_rect)


    textThree = pauseFont.render("Your total accuracy was: " + str(accuracy) + "%", True, "white")
    textThree_rect = textThree.get_rect(center=(self.width // 2, self.height // 2.4))
    self.screen.blit(textThree, textThree_rect)

    textFour= pauseFont.render("Press Escape to Quit", True, "white")
    textFour_rect = textFour.get_rect(center=(self.width // 2, self.height // 2.2))
    self.screen.blit(textFour, textFour_rect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          #data permanence
          highscore = open("assets/highscores.txt", "a")
          highscore.write("User: " + str(self.score)+"\n")
          highscore.close()
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
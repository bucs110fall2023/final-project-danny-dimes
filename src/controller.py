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
      self.width, self.height = pygame.display.get_window_size()
      self.BackGround = Background()
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
      self.instructions = pygame.font.Font(None, 35).render(
          "Shoot as many ducks as possible in 1 minute!", True, (255, 255, 255)
      )
      self.instructions_rect = self.instructions.get_rect(x=320, y=100)

      self.instructions2 = pygame.font.Font(None, 35).render(
          "Press \"P\" To Pause", True, (255, 255, 255)
      )
      self.instructions2_rect = self.instructions2.get_rect(x=320, y=140)

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
              #add to points
          self.total_shots+=1
      

      self.clock.update_clock
      if self.clock.update_clock == False: #if time = 0, go to endloop
        self.state=="END"
      
        
      self.mascots.update #update mascots
      self.scoreboard.update(self,self.score)#point variable inside
      self.shotcounter.update(self,self.total_shots)

      #redraw models
      #redraw background

      pygame.display.flip()

        #elif event.type == pygame.KEYDOWN:
          #if event.key == pygame.K_p:
            #self.state = "PAUSE"  # Pause game
              #return  # Exit the gameloop, as the game is paused
            
      # Update game objects
      self.timer.tick(self.fps)
   
    
#do cursor last

  #def pauseloop(self):
    # for event in pygame.event.get():
    #   if event.type == pygame.QUIT:
    #     self.state = "END"
    #   elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_p:
    #       self.state = "GAME"  # Resume the game
    #     # Handle other pause menu events



  #def endloop(self):
#     #when timer = 0
#    # Final Results Labels
#         self.results = pygame.font.Font(None, 35).render("", True, (255, 255, 255))
#         self.results_rect = self.results.get_rect(x=320, y=100)  # How many ducks were hit
#         self.results2 = pygame.font.Font(None, 35).render("", True, (255, 255, 255))
#         self.results2_rect = self.results2.get_rect(x=320, y=140)  # Accuracy

#                 # Check if the game time is up
#         if Game.over:
#             self.menu_counter = 0
#             self.playing = False
#             Game.over = True

#             # Show results
#             self.results.value = (
#                 "You hit " + str(Game.ducks_hit) + " of " + str(Game.total_ducks) + " ducks!"
#             )
#             self.results2.value = "Accuracy: " + str(
#                 int((int(Game.ducks_hit) / Game.total_shots) * 100)
#             ) + "%"

#             self.add(self.results)
#             self.add(self.results2)

#             self.kill()


#     pygame.quit()
#     exit()
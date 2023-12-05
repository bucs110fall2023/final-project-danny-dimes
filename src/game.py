import pygame
from livewires import games
from random import randint
from duck import Duck
from clock import Clock

class Game(games.Sprite):
    """ Duck Spawner Class """
    image = games.load_image("Sprites\spawner.png")

    # Scoring
    score = 0 
    ducksHit = 0
    totalShots = 0 # Total Shots Taken
    totalDucks = 0 # Total Ducks Spawned

    # State of Game
    paused = False # True when game is paused
    over = False # True when game is over
    
    # Label for total points
    scoreLabel = games.Text(value="0", size=25, left=500, y=428, color=color.white)
    games.screen.add(scoreLabel)

    # Label for number of ducks shot
    ducksShotLabel = games.Text(value="0", size=30, x=70, y=418, color=color.white)
    games.screen.add(ducksShotLabel)
    
    def __init__(self):
        super(Game, self).__init__(image=Game.image, x=0, y=0)

        # Instructions Labels
        self.instructions = games.Text(value="Shoot as many ducks as possible in 1 minute!", size=35, x=320, y=100, color=color.white)
        self.instructions2 = games.Text(value="Press \"P\" To Pause", size=35, x=320, y=140, color=color.white)
        games.screen.add(self.instructions)
        games.screen.add(self.instructions2)
        
        # Paused Game Sprite
        self.paused = games.Sprite(image=games.load_image("Sprites/paused.png"), x=320, y=240, dx=0, dy=0)
                                      
        # Final Results Labels
        self.results = games.Text(value="", size=35, x=320, y=100, color=color.white) # How many ducks were hit
        self.results2 = games.Text(value="", size=35, x=320, y=140, color=color.white)# Accuracy

        # Counters to delay events
        self.spawnCounter = 0
        self.menuCounter = 0
        
        self.keyDelay = 0
        self.keyDelayStart = False
        
        self.playing = False # Set to true after instructions go away
        
        # Create the timer for the game
        self.gameTimer = Clock()
        games.screen.add(self.gameTimer)
        
    def spawn(self):
        """ Spawn a duck """
        # Generate a radnom colored duck
        new_duck = Duck(randint(1, 3))

        Game.totalDucks += 1
            
        games.screen.add(new_duck)

    def update(self):
        # Check if the game time is up
        if Game.over:
            self.menuCounter = 0
            self.playing = False
            Game.over = True

            # Show results
            self.results.value = "You hit " + str(Game.ducksHit) + " of " + str(Game.totalDucks) + " ducks!"
            self.results2.value = "Accuracy: " + str(int((int(Game.ducksHit) / Game.totalShots) * 100)) + "%"

            games.screen.add(self.results)          
            games.screen.add(self.results2)
            
            self.destroy()
            
    def tick(self):
        if self.playing and not Game.paused and not Game.over:
            # Keep counting until the duck spawner should spawn a new duck
            self.spawnCounter += 1

            if self.spawnCounter >= 75:
                self.spawn()
                self.spawnCounter = 0
            
        elif not Game.paused and not Game.over:
            # Keep counting until the menu should dissapear
            if self.menuCounter >= 250:
                games.screen.remove(self.instructions)
                games.screen.remove(self.instructions2)
                self.menuCounter = 0
                self.playing = True
                self.gameTimer.start_clock()
                
            else:
                self.menuCounter += 1
        
        elif not Game.paused and not Game.over:
            # Keep the final results until they should dissapear
            if self.menuCounter >= 500:
                self.destroy()
                exit
                
            else:
                self.menuCounter += 1
        
        # Check for the pause button to be pressed
        if games.keyboard.is_pressed(games.K_p) and not Game.over:
            if self.keyDelay == 0:
                # Pause or unpause the game
                Game.paused = not Game.paused
                self.keyDelayStart = True
                
                # Display the pause sprite if on pause, remove if not
                if Game.paused:
                    games.screen.add(self.paused)
                    games.screen.add(self.instructions)
                                   
                else:
                    # Keep mouse at position it was in when it paused to avoid cheating
                    pygame.mouse.set_pos(Cursor.xPos, Cursor.yPos)

                    # Remove pause label and instructions
                    games.screen.remove(self.paused)
                    games.screen.remove(self.instructions)
        
        # Advance the keyboard delay
        if self.keyDelayStart:
            if self.keyDelay > 10:
                self.keyDelay = 0
                self.keyDelayStart = False

            else:
                self.keyDelay += 1

    def update_score(points):
        """ Update The Game Score """
        Game.score += points
        Game.ducksHit += 1

        Game.scoreLabel.value = Game.score
        Game.ducksShotLabel.value = Game.ducksHit

        Game.scoreLabel.left = 500

from livewires import games
from random import randint

class Duck(games.Sprite):
    
    """ Duck Class """
    def __init__(self, duckType):     
        # Colors Available
        colors = [3, "black", "blue", "red"]
        duckColor = colors[duckType]
           
        # Sprites for the Duck
        self.flyRight = [3, games.load_image("Sprites/" + duckColor + "/duck1.png"), games.load_image("Sprites/" + duckColor + "/duck2.png"),
                            games.load_image("Sprites/" + duckColor + "/duck3.png")]
        
        self.flyStraightRight = [3, games.load_image("Sprites/" + duckColor + "/duck4.png"), games.load_image("Sprites/" + duckColor + "/duck5.png"),
                                    games.load_image("Sprites/" + duckColor + "/duck6.png")]

        self.flyLeft = [3, games.load_image("Sprites/" + duckColor + "/duck7.png"), games.load_image("Sprites/" + duckColor + "/duck8.png"),
                           games.load_image("Sprites/" + duckColor + "/duck9.png")]

        self.flyStraightLeft = [3, games.load_image("Sprites/" + duckColor + "/duck10.png"), games.load_image("Sprites/" + duckColor + "/duck11.png"),
                                   games.load_image("Sprites/" + duckColor + "/duck12.png")]

        self.die = [3, games.load_image("Sprites/" + duckColor + "/duckDie1.png"), games.load_image("Sprites/" + duckColor + "/duckDie2.png"),
                       games.load_image("Sprites/" + duckColor + "/duckDie3.png")]

        # Intialize Duck Sprite At Random X-Location
        super(Duck, self).__init__(image=self.flyRight[1], x=randint(10, 470), y=350, dx=0, dy=-1)
        
        # Point Values Based On Duck Color
        pointValues = {"blue": 25, "red": 50, "black": 75}
        
        # Direction Constants
        self.RIGHT = 1
        self.LEFT = 2
        
        # Duck Variables
        self.alive = True
        self.direction = randint(1, 2)
        self.straight = False # True if duck is flying straight
        self.points = pointValues[duckColor]
        
        # Animation Frames
        self.frames = [4, self.flyRight[2], self.flyRight[3], self.flyRight[2], self.flyRight[1]]
        
        # Points above the duck's head when it's shot
        self.deathScore = games.Text(value=str(self.points), size=25, x=self.x, y=self.top - 5, color=color.white)
        
        # Animation Variables
        self.dieDelay = 0 # Delay Duck Falling
        self.continueDeath = False
        self.animationCount = 0
        self.frame = 1 # What frame of the animation?
        self.directionCount = 0
        
        # Set velocity based on direction
        if self.direction == self.RIGHT:
            self.dx = .5
                   
        else:
            self.dx = -.5

    def change_direction(self):
        """ Decide to change duck's direction """
        randomNum = randint(1, 340)
        
        if randomNum % 5 == 0:
            # Switch the duck's direction
            if self.direction == self.RIGHT:
                self.direction = self.LEFT
                self.dx = -.5
                
            else:
                self.direction = self.RIGHT
                self.dx = .5
        
        # Decide if it will fly straight or not
        randomNum = randint(1, 340)
        
        if randomNum % 5 == 0:
            # Change duck to straight or up
            self.straight = not self.straight
        
    def update(self):
        """ Update the sprite """
        global foreground
        
        if not Game.paused and not Game.over:
            # Check if the duck is alive
            if self.alive:
                # Duck is alive
                if self.bottom < 0 or self.right < 0 or self.left > 640:
                    # Duck is off the screen, destroy
                    self.destroy()

                # Check if the duck should try and change directions
                if self.directionCount < 100:
                    self.directionCount += 1
                
                else:
                    self.change_direction()
                    self.directionCount = 0
                
                # Check if the duck is going straight and change velocity
                if self.straight:
                    self.dy = 0
                
                    if self.direction == self.RIGHT:
                        self.dx = 1
                    
                    else:
                        self.dx = -1
                    
                else:
                    # Duck is flying upwards
                    self.dy = -1

                
                # Update the animation frames based on duck's velocity
                if not self.alive:
                    self.frames = [2, self.die[2], self.die[3]]
                    
                elif self.direction == self.RIGHT:
                    if self.straight:
                        self.frames = [4, self.flyStraightRight[2], self.flyStraightRight[3], self.flyStraightRight[2], self.flyStraightRight[1]]
                        
                    else:
                        self.frames = [4, self.flyRight[2], self.flyRight[3], self.flyRight[2], self.flyRight[1]]
                
                elif self.direction == self.LEFT:
                    if self.straight:
                        self.frames = [4, self.flyStraightLeft[2], self.flyStraightLeft[3], self.flyStraightLeft[2], self.flyStraightLeft[1]]

                    else:
                        self.frames = [4, self.flyLeft[2], self.flyLeft[3], self.flyLeft[2], self.flyLeft[1]]

                if self.frame > self.frames[0]:
                    self.frame = 1
                    
                # Check for mouse clicks
                if Cursor.clicked:
                    # Prevent the shooting of a duck that's behind the tree
                    if not (Cursor.xPos in range(150, 240) and Cursor.yPos in range(220, 390)):
                        # Check if the mouse was over the duck
                        if Cursor.xPos in range(self.left, self.right) and Cursor.yPos in range(self.top, self.bottom):
                            # Duck was shot - Kill it
                            self.shot()
                        
            else:
                # Duck is Dead, Destroy once it hits the ground
                if self.bottom > 370:
                    self.destroy()
                
    def shot(self):
        """ Kill the duck """
        Game.update_score(self.points)
        
        self.alive = False # Set the duck to dead
        
        self._replace(self.die[1]) # Replace with starting death animation
        
        self.frame = 1
        self.animationCount = 0
        
        # Freeze the duck
        self.dx = 0
        self.dy = 0
        
        # Display score above ducks head
        self.deathScore.x = self.x
        self.deathScore.y = self.top - 10
        
        games.screen.add(self.deathScore)

    def update_animation(self):
        self.animationCount += 1
        
        if self.animationCount >= 17:
            # Change animation for falling dead duck
            if not self.alive:
                if self.continueDeath:
                    self.dy = 2
                    
                    # Advance the Death Animation
                    frames = [2, self.die[3], self.die[2]]
                    
                    self._replace(frames[self.frame])

                    self.frame += 1

                    # Make Sure the frame stays within the correct range
                    if self.frame > frames[0]:
                        self.frame = 1
                
            # Change animation for duck that's not dead
            else:
                if self.frame > self.frames[0]:
                    self.frame = 1

                self._replace(self.frames[self.frame])

                self.frame += 1

                if self.frame > self.frames[0]:
                    self.frame = 1
                    
            # Reset the animation counter
            self.animationCount = 0
            
    def tick(self):
        """ Tick Method """
        # Tick only if game is not paused
        if not Game.paused:
            if not self.alive:
                # This will display the point value above the head and when it's done the duck will start to fall
                if self.dieDelay > 50 and not self.continueDeath:
                    self.dy = 1
                    
                    self.continueDeath = True
                    self.frame = 1
                    games.screen.remove(self.deathScore)

                elif not self.continueDeath:
                    self.dieDelay += 1
                    
            # This elif will help birds continue to fly
            # At the correct angle and direction after restuming from a pause
            elif (self.dx == 0) and (self.dy == -1):
                if not self.straight:
                    if self.direction == self.RIGHT:
                        self.dx = .5
                    
                    else:
                        self.dx = -.5
            
            # Update the Duck's animation
            self.update_animation()

        elif Game.paused:
            # Game is Paused - Freeze the duck
            self.dx = 0
            self.dy = 0

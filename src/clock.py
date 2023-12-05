from livewires import games
from game import Game

class Clock(games.Sprite):
    """ Class for displaying the Clock """
    def __init__(self):
        super(Clock, self).__init__(image=Game.image, x=0, y=0)

        # Timer Display
        self.timer = games.Text(value="1:00", size=50, x=300, y=435, color=color.white)
        games.screen.add(self.timer)
        
        self.clockCount = 0
        self.seconds = 60
        
        # Sound For Last 10 Seconds
        self.sound = games.load_sound("Sounds/beep.wav")

        self.started = False

    # Start the clock
    def start_clock(self):
        self.started = True
    
    def update(self):
        # Check if clock has run out of time
        if self.seconds <= 0:
            self.started = False
            Game.over = True

            games.mouse.is_visible = True # Show mouse
        
        # Change the clock's color to red when it gets down to the last minute
        if self.seconds <= 10:
            self.timer.color = color.red

        # Keep the clock in the same position
        self.timer.left = 280

    # Update the Clock's Label
    def update_clock(self):
        label = "0:"
        
        if self.seconds < 10:
            label += "0" + str(self.seconds)

        else:
            label += str(self.seconds)

        # Play sound on final 10 seconds
        if self.seconds < 11:
            self.sound.play()

        # Update The Clock's Label
        self.timer.value = label

    # Perform the Clock countdown
    def tick(self):
        # Only Do Countdown if not paused and playing the game
        if self.started and not Game.paused:
            if self.clockCount >= 100:
                self.seconds -= 1

                # Show the new time on the clock
                self.update_clock()

                self.clockCount = 1
                
            else:
                self.clockCount += 1

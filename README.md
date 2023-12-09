[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803311&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# AEC Duck Hunt
## CS110 Final Project  Fall Semester, 2023

## Team Members

Michael Icarangal, Markus Massina

***

## Project Description
A version of the classic game Duck Hunt where all the ducks are replaced by Binghamton University's rivals in the AEC! The player will have a chance to eliminate these mascots by clicking on the with the mouse over an interval of one minute! Total mascots hit and accuracy are shown in the game over screen. 

***    

## GUI Design
### Initial Design

![GUI Initial](assets/initial_design.png)

### Final Design

![GUI Final One](assets/in_game.png)

## Program Design

### Features

1. Total Points 
2. Pause 
3. Timer
4. End screen showing mascots hit/accuracy
5. Different mascots moving in different patterns

### Classes

mascot class: This represents a mascot in the Mascot Hunt game. It handles the mascot's movement
background class: Initializes game's background



## ATP
1. Test Case: Pause
- Test Description: Verify the functionality and appearance of the user interface elements. <br />
- Test Steps: <br />
1.1 Launch the game. <br />
1.2 Pause game by pressing P <br />
1.3 Unpause by pressing P again <br />
- Expected Outcome: The game pauses, showing a white screen and the word "paused" and when pressing P again the game resumes

2. Test Case: Mascot Spawning
- Test Description: Ensure mascots spawn correctly and follow patterns.
- Test Steps:
2.1 Start a new game.
2.2 Observe the spawning of mascots.
2.3 Confirm mascots move in patterns.
- Expected Outcome: Mascots spawn appropriately and move

3. Test Case: Shooting Mechanism
- Test Description: Validate the shooting mechanism and accuracy.
- Test Steps:
3.1 Start a new game.
3.2 Aim at a mascot.
3.3 Fire a shot.
- Expected Outcome: Shots accurately hit the targeted mascots, and the shooting mechanism responds appropriately.

4. Test Case: Scoring System
- Test Description: Confirm the scoring system calculates points accurately.
- Test Steps:
4.1 Start a new game.
4.2 Successfully shoot mascots.
4.3 Miss shots intentionally.
- Expected Outcome: Points are assigned correctly for successful shots, and no points are awarded for missed shots.

5. Test Case: Game Over 
- Test Description: Ensure the game ends appropriately under different scenarios.
- Test Steps:
5.1 Start a new game
5.2 Play game until timer runs out
- Expected Outcome: The game ends when the timer runs out or the player reaches the target score, displaying text showing that game is over with 
accuracy/mascots hit


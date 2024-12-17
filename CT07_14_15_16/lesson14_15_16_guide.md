# Lesson 14 - Recreate bouncing ball program using pygame

## Task 1: Pygame window
Create a pygame window with the following specifications:
1. Window width: 800
2. Window height: 600
3. Window title: 'Pong Game'
4. Window variable: 'screen'

---------------------------------------------------------------

## Task 2: Main loop
Continuing from your code in Task 1, create a main loop to keep
your window open.

Your main loop must contain the following components:
1. Handle events (e.g. closing the window)
2. Update the window
3. Quit pygame (upon exiting the loop)

---------------------------------------------------------------

## Task 3: Drawing player paddles
**Task 3a: Drawing player 1's paddle**
Using 'pygame.draw.rect(surface, color, (left, top, width,
height))':
1. Create a 20(w) x 100(h) white paddle for player 1
2. The paddle must be 10 pixels away from the left border
3. Centred vertically

**Task 3b: Drawing player 2's paddle**
Using 'pygame.draw.rect(surface, color, (left, top, width,
height))':
1. Create a 20(w) x 100(h) white paddle for player 2
2. The paddle must be 10 pixels away from the right border
3. Centred vertically

---------------------------------------------------------------

## Task 4: Controlling player paddles
**Task 4a: Controlling player 1's paddle**
Using 'keys = pygame.key.get_pressed()' to get key presses:
1. Move paddle 1 up by 1 pixel when 'w' key is pressed
2. Move paddle 1 down by 1 pixel when 's' key is pressed

Ensure that your code does not allow for the paddle to move
beyond the window.

**Task 4b: Debugging (drawn object doesn't disappear)**
1. Define the variable 'black' using the RGB value of (0, 0, 0).
2. Fill the entire screen black before drawing the objects.

**Task 4c: Controlling player 2's paddle**
1. Move paddle 2 up by 1 pixel when 'UP' key is pressed
2. Move paddle 2 down by 1 pixel when 'DOWN' key is pressed

Ensure that your code does not allow for the paddle to move
beyond the window.

---------------------------------------------------------------

## Task 5: Creating ball object
Create a ball object with the following properties:
1. Ball radius: 10
2. Ball x-coordinate: centre of window
3. Ball y-coordinate: centre of window

Then in your main loop:
1. Draw the ball object using the 'pygame.draw.circle()'
   function.

---------------------------------------------------------------

## Task 6: Moving the ball
Initialise 2 variables that will determine the speed and
direction the ball will move:
1. ball_dx = 0.5
2. ball_dy = 0.5

In your main loop:
1. Update the ball position by changing 'ball_x' and 'ball_y'
   by 'ball_dx' and 'ball_dy' respectively.

---------------------------------------------------------------

## Task 7: Ball wall bounce
**Task 7a: Y-direction**
Using an 'if' statement:
1. Check if the ball is above or below the window in the
   y-direction
2. If true, reverse the y-direction that the ball is moving

**Task 7b: X-direction**
Using an 'if' statement:
1. Check if the ball is beyond the left or right side of the
   window
2. If true, reverse the x-direction that the ball is moving

---------------------------------------------------------------

## Task 8: Bounding box + ball bounce
**Task 8a: player 1**
Create a bounding box for player 1's paddle and use it to
interact with the ball. The ball must reverse the x-direction
that it is travelling if touching paddle 1.

**Task 8b: player 2**
Create a bounding box for player 2's paddle and use it to
interact with the ball. The ball must reverse the x-direction
that it is travelling if touching paddle 2.

---------------------------------------------------------------

## Task 9: Image as a background
Using 'screen.blit()' and the uploaded 'Grass Court' jpeg image,
replace the black background with an image of a tennis court.

---------------------------------------------------------------

## Task 10: Image as a sprite (ball)
By loading and drawing the uploaded 'Tennis Ball.png', replace
the white ball with the image of a tennis ball provided.

---------------------------------------------------------------

## Task 11: Image as a sprite (racket)
**Task 11a: racket 1**
By loading and drawing the uploaded 'Tennis Racket.png',
replace player 1's white paddle with the image of the tennis
racket provided.

**Task 11b: racket 2**
By loading and drawing the uploaded 'Tennis Racket.png',
replace player 2's white paddle with the image of the tennis
racket provided.

Player 2's racket must be rotated 180 degrees.

---------------------------------------------------------------

## Task 12: Goal detection and score keeping
Create the following variables to keep track of each player's
score:
1. player1_score
2. player2_score

In your game loop, modify the code that previously detects if
the ball is too far to the left/right of the screen to:
1. Award the respective player a point depending on which side
   of the window the ball meets.
2. Announce in the console the player's latest score.

---------------------------------------------------------------

## Task 13: Drawing score on screen
**Task 13a: player 1**
Display player 1's score on the top-left corner of the screen.

**Task 13b: player 2**
Display player 2's score on the top-right corner of the screen.

---------------------------------------------------------------

## Task 14: Announcing winner
Modify your code to:
1. Define a bigger font to be used when announcing winner
2. Render "Player 1 wins!" and "Player 2 wins!" texts
3. Announce the winner by displaying the relevant text in the
   centre of the screen when one player reaches 3 points

---------------------------------------------------------------

## Task 15: Ending the game after displaying winner
Modify your code to end the game 3 seconds after announcing
the winner.

---------------------------------------------------------------

## Task 16: Reset ball position after a score
Modify your code to bring the ball back to the centre of the
screen each time a player scores.

---------------------------------------------------------------

## Task 17: Game pause after reset
Modify your code to add a 3 seconds pause to the game each time
a player scores and the ball resets.
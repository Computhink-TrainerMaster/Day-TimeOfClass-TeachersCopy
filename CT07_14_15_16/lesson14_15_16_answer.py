# 14.1 Pygame window

# Import pygame
import pygame

# Initialize Pygame
pygame.init()

# Set window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Pong Game")



# 14.2 Main loop
# Main game loop
running = True
while running:
    # Handle events (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display (optional)
    # You can add code here to draw on the screen
    
    # Update the window (make changes visible)
    pygame.display.flip()

# Quit Pygame
pygame.quit()



# 14.3a Player 1's paddle
import pygame

# Initialize Pygame
pygame.init()

# Set window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Pong Game")

# Define colors
white = (255, 255, 255)

# Define paddle properties (color, dimensions, position)
paddle_width = 20
paddle_height = 100
paddle1_x = 10  # Positioned at x=10
paddle1_y = screen_height // 2 - paddle_height // 2  # Centered vertically

# Main loop (keep window open until closed)
running = True
while running:
    # Handle events (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the paddle rectangle
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))

    # Update the window (make changes visible)
    pygame.display.flip()

# Quit Pygame
pygame.quit()



# 14.3b Player 2's paddle
import pygame

# Initialize Pygame
pygame.init()

# Set window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Pong Game")

# Define colors
white = (255, 255, 255)

# Define paddle properties (color, dimensions, position)
paddle_width = 20
paddle_height = 100
paddle1_x = 10  # Positioned at x=10
paddle1_y = screen_height // 2 - paddle_height // 2  # Centered vertically
paddle2_x = screen_width - paddle_width - 10
paddle2_y = screen_height // 2 - paddle_height // 2

# Main loop (keep window open until closed)
running = True
while running:
    # Handle events (e.g., closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the paddle rectangle
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Update the window (make changes visible)
    pygame.display.flip()

# Quit Pygame
pygame.quit()



# 15.4a Controlling player 1's paddle
# (Existing code)

# Game loop
running = True
while running:
    # Check for events (e.g., quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()

    # Move player 1 paddle up/down
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 1
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += 1

    # (Existing code)



# 15.4b Debugging (Drawn object doesn't disappear)
# (Existing code)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# (Existing code)

# Game loop
running = True
while running:
    # (Existing code)

    # Fill the screen with black before drawing anything else
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # (Existing code)



# 15.4c Controlling player 2's paddle
# (Existing code)

# Game loop
running = True
while running:
    # (Existing code)
    
    # Move player 2 paddle up/down (replace with your desired controls for Player 2)
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= 1
    if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
        paddle2_y += 1

    # (Existing code)


        
# 15.5 Creating ball object
# (Existing code)

# Define ball properties
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2

# Game loop
running = True
while running:
    # (Existing code)

    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)

    # (Existing code)



# 15.6 Moving the ball
# (Existing code)

# Define ball movement
ball_dx = 0.5
ball_dy = 0.5

# Game loop
running = True
while running:
    # (Existing code)

    # Move player 1 and 2 paddle up/down

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # (Existing code)

    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    
    # (Existing code)



# 15.7a Ball wall bounce (y-direction)
# (Existing code)

# Game loop
running = True
while running:
    # (Existing code)

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Wall collisions (bounce)
    if ball_y <= 0 or ball_y >= screen_height:
        ball_dy *= -1  # Reverse y-direction

    # (Existing code)



# 15.7b Ball wall bounce (x-direction)
# (Existing code)

# Game loop
running = True
while running:
    # (Existing code)

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Wall collisions (bounce)
    if ball_y <= 0 or ball_y >= screen_height:
        ball_dy *= -1  # Reverse y-direction
    if ball_x <= 0 or ball_x >= screen_width:
        ball_dx *= -1 # Reverse x-direction

    # (Existing code)



# 15.8a Bounding box + ball bounce (player 1)
# (Existing code)

# Game loop
running = True
while running:
    # Existing code for wall collisions
    
    # Check paddle collisions (bounce) - Using bounding boxes
    paddle1_box = pygame.Rect(paddle1_x, paddle1_y, paddle_width, paddle_height)  # Create a rectangle for paddle 1
    
    if ball_x <= paddle1_box.right + ball_radius and ball_y >= paddle1_box.top and ball_y <= paddle1_box.bottom:
    ball_dx *= -1  # Collision with paddle 1

    # (Existing code)



# 15.8b Bounding box + ball bounce (player 2)
# (Existing code)

# Game loop
running = True
while running:
    # (Existing code)

    # Check paddle collisions (bounce) - Using bounding boxes
    paddle1_box = pygame.Rect(paddle1_x, paddle1_y, paddle_width, paddle_height)  # Create a rectangle for paddle 1
    paddle2_box = pygame.Rect(paddle2_x, paddle2_y, paddle_width, paddle_height)  # Create a rectangle for paddle 2

    if ball_x <= paddle1_box.right + ball_radius and ball_y >= paddle1_box.top and ball_y <= paddle1_box.bottom:
    ball_dx *= -1  # Collision with paddle 1

    if ball_x >= paddle2_box.left - ball_radius and ball_y >= paddle2_box.top and ball_y <= paddle2_box.bottom:
    ball_dx *= -1  # Collision with paddle 2

    # (Existing code)



# 16.9 Image as a background
# Existing code to define ball movement

# Load images
background_image = pygame.image.load('CT07_14_15_16/Grass Court.jpg')

# Game loop
running = True
while running:
    # Existing code to detect collision between ball and paddles

    # screen.fill(black)  # Replaced

    # Draw the background image
    screen.blit(background_image, (0, 0))  # Draw at (0, 0) to cover the entire screen

    # Code to draw paddles and ball

    # (Existing code)



# 16.10 Adding tennis ball sprite
# Existing code to define ball movement

# Load images
background_image = pygame.image.load('CT07_14_15_16/Grass Court.jpg') # Existing code
tennis_ball_image = pygame.image.load('CT07_14_15_16/Tennis Ball.png')

# Game loop
running = True
while running:
    # Existing code to draw the background image
    
    # Draw paddles and ball
    screen.blit(tennis_ball_image, (ball_x - ball_radius, ball_y - ball_radius))
    # pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius) # Replaced

    # (Existing code)



# 16.11a Adding racket sprite for player 1
# Existing code to define ball movement

# Load images
background_image = pygame.image.load('CT07_14_15_16/Grass Court.jpg') # Existing code
tennis_ball_image = pygame.image.load('CT07_14_15_16/Tennis Ball.png') # Existing code
tennis_racket_image = pygame.image.load('CT07_14_15_16/Tennis Racket.png')

# Game loop
running = True
while running:
    # Existing code to draw the background image

    # Draw paddles and ball
    screen.blit(tennis_ball_image, (ball_x - ball_radius, ball_y - ball_radius)) # Existing code
    screen.blit(tennis_racket_image, (paddle1_x, paddle1_y)) # Tennis racket for player 1
    # pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height)) # Replaced with Tennis Racket image

    # (Existing code)



# 16.11b Adding racket sprite for player 2
import pygame # Existing code
from pygame.transform import rotate  # Import for image rotation

# (Existing code)
# Existing code to define ball movement

# Load images
background_image = pygame.image.load('CT07_14_15_16/Grass Court.jpg') # Existing code
tennis_ball_image = pygame.image.load('CT07_14_15_16/Tennis Ball.png') # Existing code
tennis_racket_image = pygame.image.load('CT07_14_15_16/Tennis Racket.png') # Existing code

# Game loop
running = True
while running:
    # Existing code to draw the background image

    # Draw paddles and ball
    screen.blit(tennis_ball_image, (ball_x - ball_radius, ball_y - ball_radius)) # Existing code
    screen.blit(tennis_racket_image, (paddle1_x, paddle1_y)) # Existing code
    screen.blit(rotate(tennis_racket_image, 180), (paddle2_x, paddle2_y)) # Rotated tennis racket for player 2
    # pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height)) # Replaced with Tennis Racket image

    # (Existing code)



# 16.12 Goal detection and score keeping (Test case: print score to console)
# Existing code to load images

# Game variables
player1_score = 0
player2_score = 0

# Game loop
running = True
while running:
    # (Existing code)

    # Replace the following:
    # if ball_x <= 0 or ball_x >= screen_width:
    #     ball_dx *= -1 # Reverse X-direction

    # With:
    # Check if ball goes past left or right side (score)
    if ball_x >= screen_width:
        ball_dx *= -1
        player1_score += 1
        print("Player 1 score: " + str(player1_score)) # For testing

    if ball_x <= 0:
        ball_dx *= -1
        player2_score += 1
        print("Player 2 score: " + str(player2_score)) # For testing

    # (Existing code)



# 16.13a Displaying player score on screen (player 1)
# Existing code to define colours

# Define fonts
score_font = pygame.font.Font(None, 32)  # Choose a font and size

# (Existing code)

# Game loop
running = True
while running:
    # Existing code to draw paddles and ball

    # Render score text (converted to strings)
    player1_score_text = score_font.render("Player 1: " + str(player1_score), True, black)

    # Display score text
    screen.blit(player1_score_text, (10, 10))  # Top-left corner

    # (Existing code)



# 16.13b Displaying player score on screen (player 2)
# Existing code to define colours

# Define fonts
score_font = pygame.font.Font(None, 32)  # Existing code

# (Existing code)

# Game loop
running = True
while running:
    # Existing code to draw paddles and ball

    # Render score text (converted to strings)
    player1_score_text = score_font.render("Player 1: " + str(player1_score), True, black) # Existing code
    player2_score_text = score_font.render("Player 2: " + str(player2_score), True, black)
    
    # Display score text
    screen.blit(player1_score_text, (10, 10))  # Existing code
    screen.blit(player2_score_text, (screen_width - player2_score_text.get_width() - 10, 10))  # Top-right corner (adjust for text width)

    # (Existing code)



# 16.14 Announce winner
# Existing code to define colours

# Define fonts
score_font = pygame.font.Font(None, 32)  # Existing code
winner_font = pygame.font.Font(None, 64)  # Bigger font to announce winner

# Render winner text (converted to strings)
player1_win_text = winner_font.render("Player 1 wins!", True, black)
player2_win_text = winner_font.render("Player 2 wins!", True, black)

# (Existing code)

# Game loop
running = True
while running:
    # Existing code to display score text

    # Display winner
    if player1_score >= 3:
        screen.blit(player1_win_text, (screen_width // 2 - player1_win_text.get_width() // 2, screen_height // 2 - player1_win_text.get_height() // 2))

    if player2_score >= 3:
        screen.blit(player2_win_text, (screen_width // 2 - player2_win_text.get_width() // 2, screen_height // 2 - player2_win_text.get_height() // 2))

    # (Existing code)



# 16.15 Ending the game after displaying winner
import pygame # Existing code
from pygame.transform import rotate # Existing code
import time # Imported to add pause to game

# (Existing code)

# Game loop
running = True
while running:
    # Existing code to check for events

    # 3s delay before ending loop
    if player1_score >= 3 or player2_score >= 3:
        time.sleep(3)
        running = False

    # (Existing code)
    
    # Display winner
    if player1_score >= 3:
        screen.blit(player1_win_text, (screen_width // 2 - player1_win_text.get_width() // 2, screen_height // 2 - player1_win_text.get_height() // 2))

    if player2_score >= 3:
        screen.blit(player2_win_text, (screen_width // 2 - player2_win_text.get_width() // 2, screen_height // 2 - player2_win_text.get_height() // 2))

    # Update the window (make changes visible)
    pygame.display.flip()



# 16.16 Resetting ball to (0, 0) after each point
# (Existing code)

# Game loop
running = True
while running:
    # Existing code to detect wall collisions (bounce)

    # Modify the following:
    # Check if ball goes past left or right side (score)
    if ball_x >= screen_width:
        ball_dx *= -1
        player1_score += 1
        # Reset ball position after a score
        ball_x = screen_width // 2
        ball_y = screen_height // 2

    if ball_x <= 0:
        ball_dx *= -1
        player2_score += 1
        # Reset ball position after a score
        ball_x = screen_width // 2
        ball_y = screen_height // 2

    # (Existing code)



# 16.17 Game pause after ball reset
# (Existing code)

# Game variables
pause = True # Adds a 3s pause to game when True

# Game loop
running = True
while running:
    # Existing code to check for events

    # Modify the following:
    # Add a 3s delay to game if pause == True
    if pause == False:
        time.sleep(3)
        pause = False
        if player1_score >= 3 or player2_score >= 3:
            running = False # End the game only if one player has a score of 3 or more

    # (Existing code)

    # Modify the following:
    # Check if ball goes past left or right side (score)
    if ball_x >= screen_width:
        ball_dx *= -1
        player1_score += 1
        pause = True
        # Reset ball position after a score
        ball_x = screen_width // 2
        ball_y = screen_height // 2

    if ball_x <= 0:
        ball_dx *= -1
        player2_score += 1
        pause = True
        # Reset ball position after a score
        ball_x = screen_width // 2
        ball_y = screen_height // 2

    # (Existing code)

    # Modify the following:
    # Display winner
    if player1_score >= 3:
        screen.blit(player1_win_text, (screen_width // 2 - player1_win_text.get_width() // 2, screen_height // 2 - player1_win_text.get_height() // 2))
        pause = True # Pauses the game for 3 seconds
    
    if player2_score >= 3:
        screen.blit(player2_win_text, (screen_width // 2 - player2_win_text.get_width() // 2, screen_height // 2 - player2_win_text.get_height() // 2))
        pause = True # Pauses the game for 3 seconds
    
    # Update the window (make changes visible)
    pygame.display.flip()
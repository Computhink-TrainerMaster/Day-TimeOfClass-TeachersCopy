#10.Recap1a
import turtle

# Create a turtle screen object
screen = turtle.Screen()

# Keep the window open until closed manually
screen.mainloop()

#10.Recap1b
import turtle

# Create a turtle screen object
screen = turtle.Screen()

# Set the window size to 600x400 pixels
screen.setup(width=600, height=400)

# Keep the window open until closed manually
screen.mainloop()

#10.Recap2
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle shape to a turtle (optional)
t.shape("turtle")

# Set the turtle color to orange
t.fillcolor("orange")

# Set the heading to face east (right)
t.seth(0)

# Forever loop to draw the square repeatedly
while True:
    for i in range(4):
        # Move forward to draw one side of the square
        t.forward(100)
        
        # Turn left by 90 degrees to face north
        t.left(90)

#10.Recap3
'''Import and use the turtle to draw a pentagon'''
import turtle

# Set up the turtle environment
window = turtle.Screen()

# Create a turtle named "pentagon"
pentagon = turtle.Turtle()

# Drawing a pentagon
for _ in range(5):
    pentagon.forward(100)  # Move the turtle forward by 100 units
    pentagon.right(72)     # Turn the turtle clockwise by 72 degrees

# To keep the window open until it is closed manually
turtle.mainloop()



# 10.1
def alert():
  """
  Prints "Motion Detected".
  """
  print("Motion Detected")

# Call the alert function
alert()



# 10.2
import turtle

# Global turtle object (avoid using global variables in larger projects)
t = turtle.Turtle()

def square():
  """
  Draws a 20x20 square at the turtle's current position (assuming a global turtle object 't').
  """
  for _ in range(4):
    t.forward(20)
    t.left(90)

# Call the square function to draw a square
square()



# 10.3
def multiply(a, b):
 """
 Prints the product of two numbers.

 Args:
     a: The first number.
     b: The second number.
 """
 product = a * b
 print(product)

# Example usage
multiply(3, 5)  # Output: 15



# 10.4
import turtle

t = turtle.Turtle()  # Create a turtle object

def drawSquare(x, y):
  """
  Draws a 20x20 square at the given coordinates (x, y).

  Args:
      x: The x-coordinate for the square's position.
      y: The y-coordinate for the square's position.
  """
  size = 20  # Size of the square

  t.penup()
  t.goto(x, y)
  t.pendown()

  for _ in range(4):
    t.forward(size)
    t.left(90)

# Example usage
drawSquare(-50, 50)

turtle.mainloop()  # Keep the window open



# 10.5
def isElderly(age):
 """
 Checks if the given age is greater than or equal to 65.

 Args:
     age: The age to check.

 Returns:
     True if the age is 65 or older, False otherwise.
 """
 return age >= 65

# Get user's age
user_age = int(input("Enter your age: "))

# Check for elderly eligibility and print message
if isElderly(user_age):
 print("You are eligible for an elderly discount.")
else:
 print("You are not eligible for an elderly discount.")



# 10.6
def turtleCoord(t):
  """
  Gets the current x and y coordinates of the turtle object.

  Args:
      t: The turtle object.

  Returns:
      A tuple containing the x and y coordinates (x, y).
  """
  x = t.xcor()
  y = t.ycor()
  return x, y

# Example usage
x, y = turtleCoord(t)
print("Turtle coordinates after drawing: " + str(x) + ", " + str(y))


    
# 10.7
import random

def whatsappMe(number):
    print("Whatsapp me at https://wa.me/65" + str(number))

"""
Generate 100 unique random 8-digit phone numbers and prints their
WhatsApp links.
"""
used_numbers = []  # Store used numbers to avoid duplicates

for _ in range(100):
  while True:
    number = random.randint(10000000, 99999999)  # Ensure 8 digits
    if number not in used_numbers:
      used_numbers.append(number)
      whatsappMe(number)  # Assuming whatsappMe function exists
      break



# 10.8
import random

def randgen(num):
  """
  This function generates a list of num random numbers,  
  prints the total count, largest and smallest number, and average.
  """
  numbers = []
  for i in range(num):
    # Generate random number between 1 and 100 (inclusive)
    number = random.randint(1, 100)
    numbers.append(number)

  # Find the largest and smallest number
  largest = max(numbers)
  smallest = min(numbers)

  # Calculate the average
  total = sum(numbers)
  average = total / len(numbers)

  # Print the results
  print("Total numbers generated:", len(numbers))
  print("Largest number:", largest)
  print("Smallest number:", smallest)
  print("Average:", average)


# Example usage
randgen(10)



# 10.9
import random

def generate_computer_move():
  """Generates a random move (rock, paper, or scissors) for the computer."""
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def determine_winner(player_move, computer_move):
  """
  Determines the winner based on player and computer moves.

  Args:
      player_move: The player's move (rock, paper, or scissors).
      computer_move: The computer's move (rock, paper, or scissors).

  Returns:
      A string indicating the winner ("You win!", "Computer wins!", or "Tie!").
  """

  # Use if statements for win conditions (easier to understand for beginners)
  if player_move == computer_move:
    return "Tie!"
  elif player_move == "rock":
    if computer_move == "scissors":
      return "You win!"
    else:
      return "Computer wins!"
  elif player_move == "paper":
    if computer_move == "rock":
      return "You win!"
    else:
      return "Computer wins!"
  elif player_move == "scissors":
    if computer_move == "paper":
      return "You win!"
    else:
      return "Computer wins!"

# Main game loop (single player vs computer)
while True:
  # Get player's move
  player_move = input("Enter your move (rock, paper, scissors): ").lower()

  # Check for valid input
  if player_move not in ["rock", "paper", "scissors"]:
    print("Invalid move. Please enter rock, paper, or scissors.")

  # Generate computer's move
  computer_move = generate_computer_move()

  # Print moves
  print("You chose: "+ player_move)
  print("Computer chose: " + computer_move)

  # Determine winner
  winner = determine_winner(player_move, computer_move)
  print(winner)

  # Ask to play again
  play_again = input("Play again? (y/n): ").lower()
  if play_again != 'y':
    break

print("Thanks for playing!")

# 10.9 (Challenge 1: Keep Score)
def determine_winner(player_move, computer_move):
  # ... (existing win condition logic)

  # Update score based on winner
  if winner == "You win!":
    player_score += 1
  elif winner == "Computer wins!":
    computer_score += 1

  # Print current score in the main loop
  print(f"Player Score: {player_score}, Computer Score: {computer_score}")

# 10.9 (Challenge 2: Single or Two-Player Mode)
def get_game_mode():
  """
  Gets the game mode (single or two-player) from the user.

  Returns:
      The game mode ("single" or "two").
  """
  while True:
    game_mode = input("Choose game mode (single or two-player): ").lower()
    if game_mode in ["single", "two"]:
      return game_mode
    else:
      print("Invalid mode. Please enter single or two-player.")

def get_player_move(player_num):
  """
  Gets the move from a player (1 or 2).

  Args:
      player_num: The player number (1 or 2).

  Returns:
      The player's move (rock, paper, or scissors).
  """
  # ... (existing logic to get player move)

def main():
  # ... (existing game loop)

  # Get game mode before starting the loop
  game_mode = get_game_mode()

  # ... (rest of the game loop)


# 10.9 (Challenge 3: Forfeit for Loser)
def get_forfeit():
  """
  Returns a random forfeit from a list.
  """
  forfeits = [
      "Sing a song!",
      "Do 10 push-ups!",
      "Tell a funny joke!",
      "Make a funny face!",
  ]
  return random.choice(forfeits)

def main():
  # ... (existing game loop)

  while True:
    # ... (existing game loop logic)

    # Check for winner and handle forfeit (single player only)
    if game_mode == "single" and (winner == "You win!" or winner == "Computer wins!"):
      loser = "Computer" if winner == "You win!" else "You"
      print(f"{loser} lost! Time for a forfeit!")
      forfeit = get_forfeit()
      print(f"{loser} must {forfeit}")

      # Ask to play again after forfeit
      play_again = input("Play again? (y/n): ").lower()
      if play_again != 'y':
        break
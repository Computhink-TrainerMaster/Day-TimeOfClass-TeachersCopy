# Lesson 13 - Tic Tac Toe Part 3

## Task 13.3f (get_player_move)
Modify your 'get_player_move' function to:
1. Take in 1 more parameter, 'current_player'. This parameter
   will determine the current player ('X' or '0').
2. Modify the code to dynamically assign either 'X' or '0' to
   the board depending on who the current player is.
3. Modify the 'print()' function to call for the current player
   e.g. "Player X, enter your move (1-9): "

**Main game loop**
1. Initiate a new variable 'current_player' and assign it 'X'
2. Include 'current_player' as an argument when calling for
   the 'get_player_move' function
3. Test your program by changing 'current_player' between 'X'
   and '0'

---------------------------------------------------------------

## Task 13.5a (switch_player)
Create a 'switch_player' function with 1 parameter,
'current_player'. The function must:
1. Return '0' if 'current_player' is 'X'
2. Else, return 'X'

**Main game loop**
1. Switch the player between 'X' and '0' after every turn.

---------------------------------------------------------------

## Task 13.mainGameLoop
Modify the main game loop to print "Player <current_player>
wins!" instead of "You win!"

---------------------------------------------------------------

## Task 13.6a (check_full)
Create a 'check_full' function that has 1 parameter, 'board'.
This function will:
1. Check if there are any available cells on the board

**Main game loop**
Make use of the 'check_full' and 'check_win' function to check
if the game is a draw.

---------------------------------------------------------------

## Ideas for other features to implement:
1. Win tracking
    - Create variable to store the number of wins for each
      player
2. 1-player mode with AI:
    - Create a function 'get_ai_move' that will do one of the
      following in order of priority:
        a. Make a winning move
        b. Make a defensive move
        c. Make a random move
3. Difficulty levels for AI:
    - Allow for the player to choose AI difficulty:
        a. Easy: Choose a random empty cell each time
        b. Medium: Prioritise blocking human player from
                   winning
        c. Hard: Implement the algorithm you have created for
                 idea #2
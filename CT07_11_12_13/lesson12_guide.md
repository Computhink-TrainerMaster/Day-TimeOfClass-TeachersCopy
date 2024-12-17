# Lesson 12 - Tic Tac Toe Part 2/3

## Task 12.3a (get_player_move)
Using the algorithm provided, create a 'get_player_move'
function with 1 parameter, 'board'.

**Algorithm**
move = int(move_input) - 1
row = move // 3
col = move % 3

When called, the function must:
1. Ask player for a number between 1 and 9 (stored in
   'move_input')
2. Apply the above algorithm to calculate the row and column
   number
3. Assign 'X' to the selected cell

**Main game loop**
1. Initialise a game board
2. Print the game board
3. Ask the user for a move

---------------------------------------------------------------

## Task 12.3b (get_player_move)
Modify your game loop to repeat steps 2 and 3 forver:
1. Initialise a game board
2. Print the game board
3. Ask the user for a move

---------------------------------------------------------------

## Task 12.3c (get_player_move)
Modify your 'get_player_move' function to:
1. Check if the user's input contains only digits before
   processing the user's input.
2. Else, print "Invalid input. Please enter a number."

---------------------------------------------------------------

## Task 12.3d (get_player_move)
Modify your 'get_player_move' function to:
1. Also check if the user's input is more than or equal to 1
   and less than or equal to 9
2. Else, print "Please enter a number between 1 and 9"

---------------------------------------------------------------

## Task 12.3e (get_player_move)
Modify your 'get_player_move' function to:
1. Check if the chosen cell is empty before assigning 'X' to
   the cell.
2. Else, print "That spot is already taken or invalid. Please
   choose another."

---------------------------------------------------------------

## Task 12.4a (check_win)
Create a 'win_conditions' list that holds each of the following
as a separate item:
1. All possible horizontal winning conditions
2. All possible vertical winning conditions
3. All possible diagonal winning conditions

There should be 8 items in total.

---------------------------------------------------------------

## Task 12.4b (check_win)
Create a 'check_win' function with 1 parameter, 'board'. This
function must:
1. Contain the 'win_conditions' list you have created earlier
2. Loop through each winning condition to check if all 3 cells
   in the winning condition are the same symbol, and are not
   spaces (' ').
3. Return 'True' if the above condition is met. Else, return
   'False'

**Main game loop**
Modify your main game loop to:
1. Check if the ‘check_win’ function returns ‘True’ or ‘False’
   after each time the ‘get_player_move’ function is called.
2. If ‘True’, call for the ‘print_board’ function before
   printing “You win!”
3. Exit the forever loop using ‘break’
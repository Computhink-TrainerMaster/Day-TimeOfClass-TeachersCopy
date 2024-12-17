# Lesson 11 - Tic Tac Toe Part 1/3

## Recap 1: diceGuess function
Create a function named 'diceGuess' with in 1 parameter,
'guess' (an integer between 1 and 6). The function returns True
if the guess matches a randomly generated number between 1 and
6, and False otherwise.

1. Import 'random' library
2. Define 'diceGuess' function with 1 parameter, 'guess'
        a. Using '.randint()', create and assign the
           'random_number' variable a random number between 1
           and 6
        b. Using 'return', return the boolean value of
           'guess == random_number'

Usage example:
if diceGuess(5):
    print("Correct!")
else:
    print("Incorrect.")

---------------------------------------------------------------

## Task 1: Tic Tac Toe Part 1
We are creating a Tic Tac Toe program and will be splitting the
program into different functions.

We will be working on each of the different functions
separately before putting all of the functions together to
bring the Tic Tac Toe program to life.

Here are the functions that we will be creating:


**Task 1a**: Initialise board
Create an 'initialise_board()' function that returns a 3x3 Tic
Tac Toe board using nested lists. Each item in each of the list
holds a space (' ').

The 3x3 nested list visualised:
[[' ', ' ', ' '],
 [' ', ' ', ' '],
 [' ', ' ', ' ']]

1. Create an 'initialise_board()' function that does the
   following
2. Create an empty list, 'board'
3. Using 'for' loop to iterate 3 times,
        a. Create an empty list, 'row'
        b. Using 'for' loop to iterate 3 times,
                i. Using '.append()', add a space (' ') into
                   the list, 'row'.
        c. Append ('.append()') the list, 'row' into the list,
           'board' to create a nested list.
5. Return 'board'

**Test case**
Input:
    print(initialise_board())
Expected output:
    [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

**Summary of function created**
Input: initialise_board()
Output: A 3x3 Tic Tac Toe board (list of lists) initialised
        with spaces
Usage: board = initialise_board()

**Task 1b**: Print board (print("", end=""))
Create a 'print_board' function with 1 parameter, 'board', that
prints the Tic Tac Toe board with cells labelled from 1 to 9.

1. Go to the next line by printing "\n" and print "Board Layout:"
2. Create a 'print_board' function that does the following
3. Create and assign the 'cell_number' variable an integer 1
4. Create a nested 'for' loop that does the following:
        Loop through each cell of each row of the board
            If cell is not a space (' '),
                print ' <cell> ' and prevent going to a new
                line by using 'end=""' in the print statement
            Else:
                print ' <cell_number> ' and prevent going to a
                new line by using 'end=""' in the print
                statement
            If 'cell_number' is not divisible by 3,
                print '|' and prevent going to a new line by
                using 'end=""' in the print statement
            Increase 'cell_number' by 1
        If 'cell_number' is less than or equals to 9,
            Go to a new line by printing "\n" and print
            "----------"
5. Do step 4 for each row of the board
6. Go to a new line by printing "\n"

**Test case**
Input:
    board = initialise_board()
    print_board(board)
Expected output:
    Board Layout:
     1 | 2 | 3 
    ----------
     4 | 5 | 6 
    ----------
     7 | 8 | 9 

**Summary of function created**
Input: print_board(board)
Output: Prints the Tic Tac Toe board
Usage: print_board(board)


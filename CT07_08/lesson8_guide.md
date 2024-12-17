# Lesson 8 - String splitting, list joining, and
#            finding substring

## Recap 1: List Manipulation
Given 3 lists, merge them into a single list, remove
duplicates, and then split the list into 2 halves,
ensuring both halves are sorted.

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]

1. Merge the 3 lists and remove duplicates.
2. Sort the resulting list.
3. Split the list into 2 sorted halves.
4. Print the halves.
5. 
---------------------------------------------------------------

## Task 1: Password Validation
A website requires all password to:
1. Be at least 8 characters long
2. Contain an upper and lower case
3. Contain a number
4. No other characters except alphabets or numbers

Task:
Write a program that will ask the user for a password, and
check if the password fits all criteria

You may use some of the following passwords to test your
program:
1. PassW0rd
2. H3ll0W0r1d
3. BestF00d
4. pa55Me

---------------------------------------------------------------

## Task 2: Mocking Text Generator6
Create a program that will turn regular sentences into a
"SpongeBob Mocking" meme.

For example, the program will turn "Hello my name is James"
into "HeLlO mY nAmE iS jAmEs"

1. Using 'input()', ask the user for a sentence
2. Use loops to iterate through each letter of the sentence
3. Alternate between '.upper()' and '.lower()' for each letter
4. Print the result

---------------------------------------------------------------

## Task 3: Splitting a Sentence into Words (.split())
**Task 3a**:
Write a program to split the following string into a list of
words using space as the delimiter:

Example:
Input:
"Computers empower our modern world with their digital brains."

Output:
['Computers',
 'empower',
 'our',
 'modern',
 'world',
 'with',
 'their',
 'digital',
 'brains.']

**Task 3b**:
Write a program to split the following string into a list of
words using a comma (,) as the delimiter:

"Computers,empower,our,modern,world,with,their,digital,brains"

Example:
Input: "Computers,empower,our,modern,world,with,their,digital,brains"
Output: ['Computers',
         'empower',
         'our',
         'modern',
         'world',
         'with',
         'their',
         'digital',
         'brains.']

---------------------------------------------------------------

## Task 4: Joining Words into a Sentence (.join())
**Task 4a**:
Given the following list of words, write a program to join
these words into a single string, separated by spaces:

['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']

Example:
Input: ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
Output: "Computers empower our modern world with their digital brains."

**Task 4b**:
Given the following list of words, write a program to join
these words into a single string, separated by commas:

['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']

Example:
Input: ['Computers', 'empower', 'our', 'modern', 'world', 'with', 'their', 'digital', 'brains.']
Output: "Computers,empower,our,modern,world,with,their,digital,brains"

---------------------------------------------------------------

## Task 5: Reversing Words in a Sentence
Create a program that takes the sentence "Hello World",
reverses each word, and then joins them back into a sentence.

1. Split the sentence "Hello World" into a list of words using
   space as the delimiter
2. Go through the list and reverse each word
3. Using space as the separator, join the list of reversed
   words back into a string
4. Print the reversed string

Example:
Sentence = "Hello World"
Output: 'olleH dlroW'

---------------------------------------------------------------

## Task 6: Checking if a Word is a Palindrome
Write a program to check if the word "radar" is a palindrome.
A word is a palindrome if it reads the same backward as forward.

Example:
Input: "radar"
Output: True

---------------------------------------------------------------

## Task 7: Checking user input for Palindrome
Create a while loop that will endlessly ask user for a word and
check if the word is a Palindrome.

The while loop will end when user says "end"

---------------------------------------------------------------

## Task 8: Checking user input for presence of Palindrome
Create a program that will check if a palindrome exists in a
sentence.

### Example:
Input:
Enter a sentence: <<"This is a sentence, check for palindrome">>

Output:
1 palindrome detected:
a
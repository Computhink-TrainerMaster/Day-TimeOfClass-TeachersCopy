# 8.Recap1
# Given lists
list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]

# Merging, removing duplicates, and sorting
merged_list = sorted(set(list1 + list2 + list3))

# Finding the midpoint and splitting
mid = len(merged_list) // 2
first_half = merged_list[:mid]
second_half = merged_list[mid:]

# Print results
print("First half:", first_half)
print("Second half:", second_half)



# 8.1
user_input = input("New password: ")

is_8char_long = False
has_upper = False
has_lower = False
has_num = False
only_alnum = False

if len(user_input) >= 8:
    is_8char_long = True

for i in user_input:
    if i.isupper() == True:
        has_upper = True

for i in user_input:
    if i.islower() == True:
        has_lower = True

for i in user_input:
    if i.isdigit() == True:
        has_num = True

if user_input.isalnum() == True:
    only_alnum = True

if is_8char_long and has_upper and has_lower and has_num and only_alnum is True:
    print("Password is valid")
else:
    print("Invalid password")



# 8.2
sentence = "Hello my name is James"
output = ""
alt = True

for i in sentence:
    if alt:
        output += i.upper()
        alt = False
    else:
        output += i.lower()
        alt = True

print(output)



# 8.3a
sentence = input("What is the sentence that you would like to split? ")
words = sentence.split()
print(words)

# 8.3b
string = "Hello,World"
words = string.split(',')
print(words)  # Output: ['Hello', 'World']



# 8.4a
words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)  # Output: 'Hello World'

# 8.4b
words = ["Hello", "World"]
sentence = ",".join(words)
print(sentence)  # Output: 'Hello,World'



# 8.5
sentence = "Hello World"
reversed_words = [word[::-1] for word in sentence.split()]
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence)  # Output: 'olleH dlroW'



# 8.6
word = "radar"
is_palindrome = word == word[::-1]
print(is_palindrome)  # Output: True



# 8.7
while True:
    user_input = input("Enter a word to check for palindrome (or type 'end' to exit): ")

    # Check if the user wants to end the loop
    if user_input == 'end':
        break

    # Output result
    if user_input == user_input[::-1]:
        print(user_input + " is a palindrome.")
    else:
        print(user_input + " is not a palindrome.")



# 8.8
# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize a list to store palindromes
palindromes = []

# Check each word
for word in words:
    # Clean the word by removing non-alphanumeric characters and converting to lowercase
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())

    # Check if the word is a palindrome
    if cleaned_word == cleaned_word[::-1] and cleaned_word != '':
        palindromes.append(cleaned_word)

# Output the result
if palindromes:
    print(f"{len(palindromes)} palindrome(s) detected:")
    for palindrome in palindromes:
        print(palindrome)
else:
    print("No palindromes detected.")
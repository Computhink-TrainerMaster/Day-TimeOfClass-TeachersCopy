# 3.Recap1
riddle_ans = "phone"
user_ans = ""

while user_ans != riddle_ans:
    user_ans = input("You answer me, although I never ask you questions. What am I? ")



# 3.1
import time

# Ask the user how many minutes they would like to study
minutes = int(input("How many minutes would you like to study? "))

# Convert minutes to seconds for the countdown
seconds = minutes * 60

# Use a while loop to count down the minutes
while seconds > 0:
    print(seconds/60)

    # Wait for 1 second
    time.sleep(60)

    # Decrease the total number of seconds by one
    seconds -= 60

# Display a motivational message once the timer is up
print("Good job!")



# 3.2
# Initialize the savings variable
savings = 0

# Using a while loop to ask how much money is saved each day
while savings < 100:
    # Ask the user for daily savings
    daily_save = float(input("How much did you save today? $"))

    # Add daily savings to total savings
    savings += daily_save

    # Check if savings goal is reached and exit the program if so
    if savings >= 100:
        print(f"Congratulations! You have saved ${savings}, which is more than $100.")
        break



# 3.3
import random

# Initialize the total questions and lives
total_questions = 15
lives = 3

for _ in range(total_questions):
    # Generate random numbers for the question
    num1 = random.randint(2, 20)
    num2 = random.randint(2, 20)
    correct_answer = num1 * num2

    # Ask the question
    while lives > 0:
        # Ask the user the question
        answer = int(input(f"What is {num1} x {num2}? "))

        if answer == correct_answer:
            print(f"Correct! {num1} x {num2} = {correct_answer}")
            break  # Move on to the next question
        else:
            lives -= 1  # Deduct a life for incorrect answer
            print(f"Wrong! Try again. You have {lives} lives left.")

        if lives == 0:
            print("GO AND SEE MS TAN FOR REMEDIAL")
            break

    if lives == 0:
        break  # Exit the quiz if no more lives are left

# If the loop is completed successfully, it means the user answered all questions correctly
if lives > 0:
    print("Congratulations! You have completed the quiz.")

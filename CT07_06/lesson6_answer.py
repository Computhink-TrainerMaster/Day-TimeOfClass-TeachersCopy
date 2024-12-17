# 6.Recap1a
import random

# Initialize an empty list to hold 100 unique random numbers
unique_numbers = []

# Using a loop to add 100 unique random numbers to the list
while len(unique_numbers) < 100:
    number = random.randint(1, 1000)  # Generate a random number between 1 and 1000
    if number not in unique_numbers:  # Ensure number is unique
        unique_numbers.append(number)

# 6.Recap1b
import random

print(max(unique_numbers))
print(min(unique_numbers))
print(sum(unique_numbers)/len(unique_numbers))
print(random.choice(unique_numbers))
print(unique_numbers.index(random.choice(unique_numbers)))



# 6.1
# Provided sample data for contacts
contacts = []
contact1 = ["John", 98453126, "john@gmail.com"]
contact2 = ["Adam", 93029102, "adam@gmail.com"]
contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# Appending each contact into the contacts list
contacts.append(contact1)
contacts.append(contact2)
contacts.append(contact3)

# Nested loop to loop through each contact and print the details
for contact in contacts:
    for detail in contact:
        print(detail)



# 6.2
# Provided sample data for students
students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]

# Loop to print out the names of each student and the gender
for student in students:
    name, gender = student  # Unpacking the list
    print("Gender of " + name + ": " + gender)



# 6.3
# Initialize lists for boys and girls
boys = []
girls = []

# Loop through the students list and separate into boys and girls
for student in students:
    name, gender = student
    if gender == "M":  # If the student is a boy
        boys.append(name)
    elif gender == "F":  # If the student is a girl
        girls.append(name)

# Count the number of boys and girls
num_boys = len(boys)
num_girls = len(girls)

print(boys, girls, num_boys, num_girls)

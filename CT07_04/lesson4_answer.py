# 4.Recap1
import time

# Initialize countdown start
countdown = 10

# Using a while loop for the countdown
while countdown > 0:
    print(countdown)
    time.sleep(1)  # Pause for 1 second
    countdown -= 1  # Decrement the countdown

print("HAPPY NEW YEAR!")  # Print the final message after countdown ends



# 4.1a
# Creating a list of 8 planets in the solar system
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]


# 4.1b
# Renaming "Mars" to a new name, let's call it "New Terra"
planets[3] = "New Terra"  # Mars is the 4th planet, so it's at index 3

# 4.1c
# Adding Pluto to the list of planets
planets.append("Pluto")

# Inserting "Lalaland" between Earth and New Terra (formerly Mars)
earth_index = planets.index("Earth")  # Get the index of Earth
planets.insert(earth_index + 1, "Lalaland")  # Inserting Lalaland right after Earth

# 4.1d
# Removing Jupiter from the list of planets
del(planets[5])



# 4.2
# Iterating through the list of planets and printing out messages based on conditions
for planet in planets:
    if planet == "Earth":
        print(f"{planet} : this is my home")
    elif planet == "New Terra":  # Mars has been renamed to New Terra
        print(f"{planet} : I conquered this")
    elif planet == "Lalaland":
        print(f"{planet} : I created this")



# 4.3
# Placeholder for a list of countries
countries = []

# Simulating user inputs as a list of countries followed by "end"
user_inputs = ["Germany", "Japan", "Brazil", "end"]

i = 0  # Index for accessing simulated user inputs
while True:
    # Simulating user input, normally you would use country = input("What country would you like to visit? ")
    country = user_inputs[i]
    i += 1  # Incrementing index for the next simulated input

    if country.lower() == "end":
        break  # Exit the loop if the user enters "end"

    # Add the country into the list
    countries.append(country)

# Print all the countries in the list in the specified format
for country in countries:
    print(f"I would like to visit {country}")



# 4.4a
# Initialize an empty list for the menu
menu = []

# Using a while loop to ask for user input
while True:
    # Ask the user to input a food item for the menu
    food_item = input("Enter a food item for the menu (type 'end' to finish): ")

    # Check if the user wants to end the input process
    if food_item == "end":
        break

    # Add the food item to the menu
    menu.append(food_item)

# Output the final menu
print("The final menu is:")
for item in menu:
    print("- " + item)

# 4.4b
customer_choice = input("What would you like to eat? ")

# Initialize a variable to track if the item is found
item_found = False

# Loop through each item in the menu to check if the item exists
for item in menu:
    if item == customer_choice:
        item_found = True
        break  # Exit loop if item is found

# Checking if the food is in the menu using the flag
if item_found:
    print("Yes we sell that, please have a seat")
else:
    print("Sorry, please go next door, bye.")
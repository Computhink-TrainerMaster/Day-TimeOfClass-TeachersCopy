# 5.Recap1a
favourite_foods = ["Pizza", "Burger", "Ice Cream", "Sushi", "Pasta"]

# 5.Recap1b
del favourite_foods[2]  # Ice Cream is the third item

# 5.Recap1c
favourite_foods.append("Tacos")

# 5.Recap1d
for food in favourite_foods:
    print(food)



# 5.1
# Importing random library for generating random numbers
import random

# Initialize an empty list to hold 100 random numbers
random_numbers = []

# Using a loop to add 100 random numbers to the list
for _ in range(100):
    number = random.randint(1, 1000)  # Generate a random number between 1 and 1000
    random_numbers.append(number)  # Add the number to the list

# Output the list of random numbers
random_numbers[:10]  # Displaying only the first 10 numbers for brevity



# 5.2
# Initialize an empty list to hold 100 unique random numbers
unique_random_numbers = []

# Using a loop to add 100 unique random numbers to the list
while len(unique_random_numbers) < 100:
    number = random.randint(1, 1000)  # Generate a random number between 1 and 1000
    # Check if the number is already in the list, if not, add it
    if number not in unique_random_numbers:
        unique_random_numbers.append(number)

# Output the list of unique random numbers
unique_random_numbers[:10]  # Displaying only the first 10 numbers for brevity



# 5.3
# Create a sample list of scores
scores = [75, 88, 92, 65, 78, 83, 95, 70, 85, 90]

# Find the maximum and minimum scores using min() and max()
max_score = max(scores)
min_score = min(scores)
average_score = sum(score) / len(scores)

# Print the results
print(f"Maximum score: {max_score}")
print(f"Minimum score: {min_score}")
print(f"Average score: {average_score}")



# 5.4
# Provided sample data
namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan", "Sophia", "Lucas", "Mia", "Aiden"]
heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# Determine the tallest person
tallest_height = max(heightlist)
tallest_index = heightlist.index(tallest_height)
tallest_name = namelist[tallest_index]

# Determine the shortest person
shortest_height = min(heightlist)
shortest_index = heightlist.index(shortest_height)
shortest_name = namelist[shortest_index]

print(tallest_name, tallest_height, shortest_name, shortest_height)



# 5.5
import random

# Provided sample data
pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]

# Choosing 2 random pokemons
pokemon1 = random.choice(pokemons)
pokemon1_index = pokemons.index(pokemon1)
pokemon1_power = powers[pokemon1_index]

pokemon2 = random.choice(pokemons)
while pokemon1 == pokemon2:  # Ensure the second pokemon is different
    pokemon2 = random.choice(pokemons)
pokemon2_index = pokemons.index(pokemon2)
pokemon2_power = powers[pokemon2_index]

# Calculating the winner
winner = pokemon1 if pokemon1_power > pokemon2_power else pokemon2

print(pokemon1, pokemon1_power, pokemon2, pokemon2_power, winner)

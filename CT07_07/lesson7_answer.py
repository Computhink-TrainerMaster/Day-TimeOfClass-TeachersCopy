# 7.Recap1
# Create a list variable called students
students = []

# Create 3 lists called student1, student2, student3
student1 = ["Alice", "987654321", "Basketball"]
student2 = ["Bob", "123456789", "Chess"]
student3 = ["Charlie", "456789012", "Robotics"]

# Add student1, student2, student3 into the students list
students.append(student1)
students.append(student2)
students.append(student3)

# Write a nested loop to loop through each student and print the details for each student
for student in students:
    name, number, cca = student
    print("Name: " + name)
    print("Phone number: " + number)
    print("CCA: " + cca)



# 7.1
# Given lists
list1 = ["Apple", "Banana", "Cherry"]
list2 = ["Durian", "Elderberry", "Figs"]

# Merging lists
merged_list = list1 + list2

# Print result
print(merged_list)



# 7.2
# Given lists
list1 = [3.20, 2.65, 1.75]
list2 = [6.15, 5.45, 4.20]

# Merging and sorting lists
sorted_list = sorted(list1 + list2)

# Print result
print(sorted_list)



# 7.3
# Given list and index
fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
index = 3

# Splitting list
left = fruits[:index]
right = fruits[index:]

# Print results
print("Left side:", left)
print("Right side:", right)



# 7.4
# Given list
fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# Finding the midpoint
mid = len(fruits) // 2

# Splitting the list
first_half = fruits[:mid]
second_half = fruits[mid:]

# Print results
print("First half:", first_half)
print("Second half:", second_half)



# 7.5
# Given lists
list1 = ["Apple", "Banana", "Cherry", "Durian"]
list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

common = []

# Finding common elements
for item in list1:
    if item in list2:
        common.append(item)

# Print result
print(common)



# 7.6
# Given lists
list1 = ["Apple", "Banana", "Cherry", "Cherry"]
list2 = ["Cherry", "Durian", "Durian", "Figs"]

unique = []

# Finding unique elements
for item in list1:
    if item not in list2:
        unique.append(item)

for item in list2:
    if item not in list1:
        unique.append(item)

# Print result
print(unique)



# 7.7
# Given lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

even = []

# Merging with condition
merged = list1 + list2

for item in merged:
    if item % 2 == 0:
        even.append(item)

# Print result
print(even)



# 7.8
nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = []

# Loop through each sublist and append each element to the flat_list
for sublist in nested_list:
  for element in sublist:
    flat_list.append(element)

print(flat_list)



# 7.9
# Given list and size
students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3

# Creating sublists without using list comprehension
sublists = []
for i in range(0, len(students), size):
    sublists.append(students[i:i+size])

# Print result
print(sublists)

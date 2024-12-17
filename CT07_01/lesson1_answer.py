# 1.Recap1
# create "glass" bin
# create "plastic" bin
# create "paper" bin

# repeat until there is no more items
#     if item is glass
#         put into "glass" bin
#     if item is plastic
#         put into "plastic" bin
#     if item is paper
#         put into "paper" bin
#     or else
#         discard item



# 1.Recap2
px_red = 1
px_blue = 2
px_green = 3

num_red = 3
num_blue = 5
num_green = 4

total = (px_red * num_red) + (px_blue * num_blue) + (px_green * num_green)

print(total)



# 1.Recap3
score_one = 80
score_two = 90
score_three = 75

total = score_one + score_two + score_three

average_score = total / 3

student_name = "Alex"

print("Average score for " + student_name + " is: " + str(average_score))



# 1.Recap4
score = int(input("Input score: "))

if score >= 75:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade: " + str(grade))
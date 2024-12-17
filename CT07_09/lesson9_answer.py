# 9.Recap1
# Ask user riddle
userInput = input("What has to be broken before you can use it? ")

# Variable to check if user got the correct answer
isCorrect = False

# Cleaning up response
userInputLower = userInput.lower()
words = userInputLower.split()

# Checking if response contains answer
for word in words:
    if word == "egg":
        isCorrect = True

if isCorrect:
    print("Correct! Well done.")
else:
    print("That's not correct. Try again!")



# 9.1a
import turtle

window = turtle.Screen()
window.setup(width=600,height=600)
window.bgcolor("forestgreen")

window.mainloop()



# 9.1b
# import turtle

# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

pen = turtle.Turtle()
pen.penup()
pen.shape("square")
pen.color("black")
pen.sety(250)

for i in range(-300,300,25):
    pen.setx(i)
    pen.stamp()

window.mainloop()



# 9.1c
# import turtle

# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

# pen = turtle.Turtle()
# pen.penup()
# pen.shape("square")
# pen.color("black")
# pen.sety(250)

# for i in range(-300,300,25):
#     pen.setx(i)
#     pen.stamp()

pen.goto(-300, -250)
pen.pendown()
pen.color("yellow")
pen.seth(0)
pen.forward(600)
pen.hideturtle()

window.mainloop()



# 9.1d
# import turtle

# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

# pen = turtle.Turtle()
# pen.penup()
# pen.shape("square")
# pen.color("black")
# pen.sety(250)

# for i in range(-300,300,25):
#     pen.setx(i)
#     pen.stamp()

# pen.goto(-300, -250)
# pen.pendown()
# pen.color("yellow")
# pen.seth(0)
# pen.forward(600)
# pen.hideturtle()

# Create Sally the Turtle
Sally = turtle.Turtle()

Sally.penup()

# Configure Sally
Sally.seth(90)
Sally.shape("turtle")
Sally.color("red")

# Move Sally to the starting point
Sally.goto(0,-250)

# Put "Sally" above Sally the turtle
Sally.write("Sally",align="center",font=('Arial',20))

window.mainloop()



# 9.1e
# import turtle

# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

# pen = turtle.Turtle()
# pen.penup()
# pen.shape("square")
# pen.color("black")
# pen.sety(250)

# for i in range(-300,300,25):
#     pen.setx(i)
#     pen.stamp()

# pen.goto(-300, -250)
# pen.pendown()
# pen.color("yellow")
# pen.seth(0)
# pen.forward(600)
# pen.hideturtle()

Bob = turtle.Turtle()
# Sally = turtle.Turtle()
Keith = turtle.Turtle()

Bob.penup()
# Sally.penup()
Keith.penup()

Bob.seth(90)
Bob.shape("turtle")
Bob.color("blue")
# Sally.seth(90)
# Sally.shape("turtle")
# Sally.color("red")
Keith.seth(90)
Keith.shape("turtle")
Keith.color("white")


Bob.goto(-200,-250)
# Sally.goto(0,-250)
Keith.goto(200,-250)

Bob.write("Bob",align="center",font=('Arial',20))
# Sally.write("Sally",align="center",font=('Arial',20))
Keith.write("Keith",align="center",font=('Arial',20))

window.mainloop()



# 9.1f
# import turtle

# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

# pen = turtle.Turtle()
# pen.penup()
# pen.shape("square")
# pen.color("black")
# pen.sety(250)

# for i in range(-300,300,25):
#     pen.setx(i)
#     pen.stamp()

# pen.goto(-300, -250)
# pen.pendown()
# pen.color("yellow")
# pen.seth(0)
# pen.forward(600)
# pen.hideturtle()

# Bob = turtle.Turtle()
# Sally = turtle.Turtle()
# Keith = turtle.Turtle()

# Bob.penup()
# Sally.penup()
# Keith.penup()

# Bob.seth(90)
# Bob.shape("turtle")
# Bob.color("blue")
# Sally.seth(90)
# Sally.shape("turtle")
# Sally.color("red")
# Keith.seth(90)
# Keith.shape("turtle")
# Keith.color("white")


# Bob.goto(-200,-250)
# Sally.goto(0,-250)
# Keith.goto(200,-250)

# Bob.write("Bob",align="center",font=('Arial',20))
# Sally.write("Sally",align="center",font=('Arial',20))
# Keith.write("Keith",align="center",font=('Arial',20))

guess = input("Guess the winner!")

window.mainloop()



# 9.7
# import turtle
import random

# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

# pen = turtle.Turtle()
# pen.penup()
# pen.shape("square")
# pen.color("black")
# pen.sety(250)

# for i in range(-300,300,25):
#     pen.setx(i)
#     pen.stamp()

# pen.goto(-300, -250)
# pen.pendown()
# pen.color("yellow")
# pen.seth(0)
# pen.forward(600)
# pen.hideturtle()

# Bob = turtle.Turtle()
# Sally = turtle.Turtle()
# Keith = turtle.Turtle()

# Bob.penup()
# Sally.penup()
# Keith.penup()

# Bob.seth(90)
# Bob.shape("turtle")
# Bob.color("blue")
# Sally.seth(90)
# Sally.shape("turtle")
# Sally.color("red")
# Keith.seth(90)
# Keith.shape("turtle")
# Keith.color("white")


# Bob.goto(-200,-250)
# Sally.goto(0,-250)
# Keith.goto(200,-250)

# Bob.write("Bob",align="center",font=('Arial',20))
# Sally.write("Sally",align="center",font=('Arial',20))
# Keith.write("Keith",align="center",font=('Arial',20))

# guess = input("Guess the winner!")

winner = ""

Bob.pendown()
Sally.pendown()
Keith.pendown()

while True:
    Bob.seth(random.randint(75,115))
    Keith.seth(random.randint(75,115))
    Sally.seth(random.randint(75,115))

    Bob.forward(random.randint(1,20))
    Keith.forward(random.randint(1,20))
    Sally.forward(random.randint(1,20))

    if Keith.ycor()>250:
        winner = "Keith"
        break
    elif Sally.ycor()>250:
        winner = "Sally"
        break
    elif Bob.ycor()>250:
        winner = "Bob"
        break

window.mainloop()



# 9.8
# import turtle
# import random

# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

# pen = turtle.Turtle()
# pen.penup()
# pen.shape("square")
# pen.color("black")
# pen.sety(250)

# for i in range(-300,300,25):
#     pen.setx(i)
#     pen.stamp()

# pen.goto(-300, -250)
# pen.pendown()
# pen.color("yellow")
# pen.seth(0)
# pen.forward(600)
# pen.hideturtle()

# Bob = turtle.Turtle()
# Sally = turtle.Turtle()
# Keith = turtle.Turtle()

# Bob.penup()
# Sally.penup()
# Keith.penup()

# Bob.seth(90)
# Bob.shape("turtle")
# Bob.color("blue")
# Sally.seth(90)
# Sally.shape("turtle")
# Sally.color("red")
# Keith.seth(90)
# Keith.shape("turtle")
# Keith.color("white")


# Bob.goto(-200,-250)
# Sally.goto(0,-250)
# Keith.goto(200,-250)

# Bob.write("Bob",align="center",font=('Arial',20))
# Sally.write("Sally",align="center",font=('Arial',20))
# Keith.write("Keith",align="center",font=('Arial',20))

# guess = input("Guess the winner!")
# winner = ""

# Bob.pendown()
# Sally.pendown()
# Keith.pendown()

# while True:
#     Bob.seth(random.randint(75,115))
#     Keith.seth(random.randint(75,115))
#     Sally.seth(random.randint(75,115))

#     Bob.forward(random.randint(1,20))
#     Keith.forward(random.randint(1,20))
#     Sally.forward(random.randint(1,20))

#     if Keith.ycor()>250:
#         winner = "Keith"
#         break
#     elif Sally.ycor()>250:
#         winner = "Sally"
#         break
#     elif Bob.ycor()>250:
#         winner = "Bob"
#         break

if guess == winner:
    print ("Your guess was correct!")
else:
    print("The winner was " + winner)
    print("Better luck next time!")

window.mainloop()

# ---------------------------------------------------------------

# Final Game:
import turtle
import random

window = turtle.Screen()
window.setup(width=600,height=600)
window.bgcolor("forestgreen")

pen = turtle.Turtle()
pen.penup()
pen.shape("square")
pen.color("black")
pen.sety(250)

for i in range(-300,300,25):
    pen.setx(i)
    pen.stamp()

pen.goto(-300, -250)
pen.pendown()
pen.color("yellow")
pen.seth(0)
pen.forward(600)
pen.hideturtle()

Bob = turtle.Turtle()
Sally = turtle.Turtle()
Keith = turtle.Turtle()

Bob.penup()
Sally.penup()
Keith.penup()

Bob.seth(90)
Bob.shape("turtle")
Bob.color("blue")
Sally.seth(90)
Sally.shape("turtle")
Sally.color("red")
Keith.seth(90)
Keith.shape("turtle")
Keith.color("white")


Bob.goto(-200,-250)
Sally.goto(0,-250)
Keith.goto(200,-250)

Bob.write("Bob",align="center",font=('Arial',20))
Sally.write("Sally",align="center",font=('Arial',20))
Keith.write("Keith",align="center",font=('Arial',20))

guess = input("Guess the winner!")
winner = ""

Bob.pendown()
Sally.pendown()
Keith.pendown()

while True:
    Bob.seth(random.randint(75,115))
    Keith.seth(random.randint(75,115))
    Sally.seth(random.randint(75,115))

    Bob.forward(random.randint(1,20))
    Keith.forward(random.randint(1,20))
    Sally.forward(random.randint(1,20))

    if Keith.ycor()>250:
        winner = "Keith"
        break
    elif Sally.ycor()>250:
        winner = "Sally"
        break
    elif Bob.ycor()>250:
        winner = "Bob"
        break

if guess == winner:
    print ("Your guess was correct!")
else:
    print("The winner was " + winner)
    print("Better luck next time!")
    
window.mainloop()
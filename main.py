from turtle import Turtle, Screen
import random

# Etch-A-Sketch
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("SkyBlue")
# screen = Screen()
#
#
# def move_forward():
#     timmy.forward(10)
#
#
# def move_backward():
#     timmy.backward(10)
#
#
# def counter_clockwise():
#     timmy.left(10)
#
#
# def clockwise():
#     timmy.right(10)
#
#
# def reset():
#     timmy.clear()
#     timmy.teleport(0, 0)
#
#
# screen.listen()
# screen.onkeypress(key='w', fun=move_forward)
# screen.onkeypress(key='s', fun=move_backward)
# screen.onkeypress(key='a', fun=counter_clockwise)
# screen.onkeypress(key='d', fun=clockwise)
# screen.onkeypress(key='c', fun=reset)
# screen.exitonclick()

screen = Screen()
screen.setup(600, 600)

user_guess = screen.textinput("Make your bet", "Which turtle will win the race? (purple, blue, green, gold, orange, red): ")

colors = ["purple", "blue", "green", "gold", "orange", "red"]
all_turtles = []

x = -270
y = 315

for turtle in range(0, 6):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    y -= 90
    tim.goto(x, y)
    tim.color(colors[turtle])
    all_turtles.append(tim)

if user_guess:
    continue_race = True

while continue_race:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 270:
            continue_race = False
            winning_turtle = turtle.pencolor()

if winning_turtle == user_guess.lower():
    print(f"You've won! The {winning_turtle} turtle is the winner!")
else:
    print(f"Oops, you've lost. The {winning_turtle} turtle is the winner.")

screen.exitonclick()
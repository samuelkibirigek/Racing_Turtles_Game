from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your BET!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "orange", "purple"]
y_position = [120, 60, 0, -60, -120]
turtles = []

for object_loop in range(5):
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.penup()
    turtle_obj.color(colors[object_loop])
    turtle_obj.goto(x=-230, y=y_position[object_loop])
    turtles.append(turtle_obj)

race_is_on = True
while race_is_on:
    for turtle in turtles:
        turtle.forward(random.choice(range(1, 10)))
        if turtle.xcor() > 205:
            race_is_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet.lower():
                print(f"You win! The {winning_color} you bet on won.")
            elif winning_color() != user_bet.lower():
                print(f"You lose! The {winning_color} you never bet on won.")


screen.exitonclick()

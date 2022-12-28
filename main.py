from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="You have a variety of colored turtle.", prompt="What turtle do you bet on?")
print(user_choice)
turtles = []


def setup(turtle_obj, shade, y):
    turtle_obj
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.color(shade)
    turtle_obj.penup()
    turtle_obj.goto(-230, y)
    turtles.append(turtle_obj)


setup(turtle_obj="tim", shade="blue", y=0)
setup(turtle_obj="jim", shade="grey", y=60)
setup(turtle_obj="tom", shade="red", y=120)
setup(turtle_obj="sam", shade="orange", y=-60)
setup(turtle_obj="kim", shade="purple", y=-120)

race_is_on = True
while race_is_on:
    for turtle in turtles:
        if turtle.xcor() < 230:
            turtle.forward(random.randint(1, 10))
        else:
            race_is_on = False
            if turtle.pencolor() == user_choice.lower():
                print(f"You win, the fastest turtle was {turtle.pencolor()}")
            elif turtle.pencolor() != user_choice.lower():
                print(f"You lose, the fastest turtle was {turtle.pencolor()}")

screen.exitonclick()

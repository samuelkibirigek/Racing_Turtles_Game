from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="You have a variety of colored turtle.", prompt="What turtle do you bet on?")
print(user_choice)
turtles = []


def setup(turtle_object, shade, y):
    turtle_object = Turtle(shape="turtle")
    turtle_object.color(shade)
    turtle_object.penup()
    turtle_object.goto(-230, y)
    turtles.append(turtle_object)
    print(turtle_object)


setup(turtle_object="tim", shade="blue", y=0)
setup(turtle_object="jim", shade="grey", y=60)
setup(turtle_object="tom", shade="red", y=120)
setup(turtle_object="sam", shade="orange", y=-60)
setup(turtle_object="kim", shade="purple", y=-120)

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

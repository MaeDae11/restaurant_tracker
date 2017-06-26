from turtle import *

def draw_square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

def fly_turtle():
    up()
    forward(100)
    right(90)
    forward(100)
    down()

def start_turtle_position():
    up()
    forward(50)
    left(90)
    forward (50)
    left(90)
    down()

def draw_star():
    for i in range(5):
        forward(100)
        right(144)    


def main():
    start_turtle_position()
    # draw_square()
    # fly_turtle()
    draw_star()

    # draw_square()
    # fly_turtle()

    # draw_square()
    # fly_turtle()

main()    
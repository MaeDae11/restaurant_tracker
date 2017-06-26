from turtle import *

def start_turtle_position():
    up()
    forward(50)
    left(90)
    forward (50)
    left(90)
    down()

def draw_triangle():
    for i in range(3):
        forward(100)
        left(120)

def main():
    draw_triangle()
    start_turtle_position()

main()    

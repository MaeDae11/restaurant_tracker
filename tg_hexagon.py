from turtle import *

def start_turtle():
    up()
    forward(50)
    left(90)
    forward(100)
    left(90)
    down()

def draw_hexagon():
    for i in range(6):
        forward(100)
        right(60)

def main():
    start_turtle():
    draw_hexagon():

main()    


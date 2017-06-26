from turtle import *

def start_turtle():
    up()
    forward(50)
    left(90)
    forward(100)
    left(90)
    down()

def turtle_square():
    for i in range(4):
        forward(100)
        left(90)

def main():
    start_turtle()
    turtle_square()

main()    
        
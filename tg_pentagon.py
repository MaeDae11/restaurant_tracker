from turtle import *

def start_turtle():
    up()
    forward(50)
    left(90)
    right(45)
    down()

def turtle_pentagon():
    for i in range(5):
        forward(100)
        left(72)
    

def main():
    start_turtle()
    turtle_pentagon()


main()            

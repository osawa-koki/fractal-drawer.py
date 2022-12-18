from turtle import *

step = 10

def draw(depth, angle):
    if depth <= 0:
        return
    right(angle)
    draw(depth - 1, -angle)
    forward(step)
    left(angle)
    draw(depth - 1,  angle)
    forward(step)
    draw(depth - 1,  angle)
    left(angle)
    forward(step)
    draw(depth - 1, -angle)
    right(angle)

color('firebrick')
draw(5, 90)
input()

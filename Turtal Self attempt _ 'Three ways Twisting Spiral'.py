'''
    '   TURTAL GRAPHICS ( self )  '
    - Three ways Twisting Spiral -
'''

import turtle

turtle.bgcolor("black")
turtle.bgcolor("black")
turtle.pencolor("white")
turtle.speed(0)

c = 0
d = 0
while True:
    for i in range(4):
        turtle.forward(80)
        turtle.right(90)
    turtle.right(5)
    c += 1
    if c >= 360/15:
        turtle.forward(50)
        c = 0
        d += 1
        if d >= 12:
            break

#turtle.hideturtle()
turtle.done()
'''
https://www.youtube.com/watch?v=jNmM3lu-y5g
    '   TURTAL GRAPHICS INTRO   '
'''

import turtle as tt

tt.bgcolor("black")
tt.pencolor("white")
tt.speed(0)

# for i in range(8):
#     for i in range(20):
#         for i in range(4):
#             tt.forward(80)
#             tt.right(90)
#         tt.left(10)
#     tt.right(2)

c = 0
while True:
    for i in range(4):
        tt.forward(80)
        tt.right(90)
    tt.right(5)
    c += 1
    if c >= 360/5:
        break

tt.hideturtle()
#tt.done()

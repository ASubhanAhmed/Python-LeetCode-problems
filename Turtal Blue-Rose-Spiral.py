'''
https://www.youtube.com/watch?v=FZ4nipl7rfM
    'TURTAL GRAPHICS'
'''
import turtle as tt

tt.bgcolor("black")
tt.speed(0)
tt.pensize(2)
tt.pencolor("blue")

def drawCircle(radius):
    for i in range(10):
        tt.circle(radius)
        radius = radius - 4
        
def design():
    for i in range(10):
        drawCircle(150)
        tt.right(36)
        
design()
tt.done()
#tt.hideturtle()

"""     Disable Line 20 & Comment out Line 19 if
        you want to automatically Close 'python turtle graphic'
        window.
"""
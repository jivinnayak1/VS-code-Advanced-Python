import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue") 

t = turtle.Turtle()
t.speed(1)

def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

def draw_rectangle():
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)

def draw_hexagon():
    for _ in range(6):
        t.forward(100)
        t.left(60)

draw_triangle()
t.penup()
t.goto(200, 0)
t.pendown()
draw_rectangle()
t.penup()
t.goto(-200, 0)
t.pendown()
draw_hexagon()

turtle.done()
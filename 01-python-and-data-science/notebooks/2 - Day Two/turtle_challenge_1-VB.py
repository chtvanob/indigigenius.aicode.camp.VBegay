import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()

# Challenge 1: Squares in a Grid

# YOUR CODE HERE
t.setheading(0)

# Make a function to draw a swuare

size = 20


def square(size):
        t.pendown()
        for i in range(4):
            t.forward(size)
            t.right(90)
        t.penup()

t.penup()
t.setposition(-50, 50)
square(20)
t.setposition(-10, 50)
square(20)
t.setposition(30, 50)

t.penup()
t.setposition(-50, 10)
square(20)
t.setposition(-10, 10)
square(20)
t.setposition(30, 10)

t.penup()
t.setposition(-50, -30)
square(20)
t.setposition(-10, -30)
square(20)
t.setposition(30, -30)

t.setposition(-60, 60)
square(120)


square(20)
square(50)
square(100)

# DON'T TOUCH THIS
turtle.mainloop()
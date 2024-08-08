import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()

# Challenge 2: Circles in a Grid with One Missing

# YOUR CODE HERE
def square(size):
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.penup()

t.penup()
t.setposition(-50,50)
t.pendown()
t.circle(10)
t.penup()
t.setposition(-10,50)
t.pendown()
t.circle(10)
t.penup()
t.setposition(30,50)
t.pendown()
t.circle(10)

t.penup()
t.setposition(-50,10)
t.pendown()
t.circle(10)
t.penup()
t.setposition(-10,10)
t.pendown()
t.circle(10)
t.penup()
t.setposition(30,10)
t.pendown()
t.circle(10)

t.penup()
t.setposition(-50,-30)
t.pendown()
# t.circle(10)
t.penup()
t.setposition(-10,-30)
t.pendown()
t.circle(10)
t.penup()
t.setposition(30,-30)
t.pendown()
t.circle(10)
t.penup()

t.setposition(-70, 80)
square(120)

# DON'T TOUCH THIS
turtle.mainloop()
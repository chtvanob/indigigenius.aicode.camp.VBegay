import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()



def draw_square(center_x, center_y, side_length=40):
    t.penup()
# t.forward(20) q   

for side in range(4):
        t.forward(side_length)
        t.right(90)

t.setheading(0)

# for _ in range(50):
    # t.right(30)

turtle.mainloop()

# Exercise 1
# Draw a Square 


# Exercise 2
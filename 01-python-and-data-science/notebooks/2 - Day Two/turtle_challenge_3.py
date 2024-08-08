import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()

# Challenge 2: Create a Function for an N-Sided Star

def draw_n_sided_star(t, n):
    # YOUR CODE HERE
    angle = 180 - (360 / (n * 2))
    for i in (n):
        t.forward(100)
        t.right(144)

draw_n_sided_star(t,5)


# DON'T TOUCH THIS
turtle.mainloop()
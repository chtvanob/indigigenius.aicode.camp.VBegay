import turtle

def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle named "t"
    t = turtle.Turtle()
    t.speed(1)  # Set the speed of the turtleimport turtle

def draw_star(t, size):
    angle = 144
    for _ in range(5):
        t.forward(size)
        t.right(angle)
        t.penup()
        t.forward(size)
        t.pendown()
        t.left(2 * angle)

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle named "t"
    t = turtle.Turtle()
    t.speed(1)  # Set the speed of the turtle

    # Define the size of the star
    size = 100

    # Draw the star
    draw_star(t, size)

    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

    # Define the size of the star
    size = 100

    # Draw the star
    draw_star(t, size)

    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
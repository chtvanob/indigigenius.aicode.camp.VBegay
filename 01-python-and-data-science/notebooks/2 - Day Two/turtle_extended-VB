import turtle

def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle named "t"
    t = turtle.Turtle()
    t.speed(1)  # Set the speed of the turtle

    # Define the width and height of the rectangles
    width = 100
    height = 50

    # Initial position
    x_start = -200
    y_start = 100

    # Draw 9 rectangles
    for i in range(3):  # Rows
        for j in range(3):  # Columns
            t.penup()
            t.goto(x_start + j * (width + 20), y_start - i * (height + 20))
            t.pendown()
            draw_rectangle(t, width, height)

    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

import turtle

class Turtle_Extended(turtle.Turtle):
    def __init__(self, shape='classic', undobuffersize=1000, visible=True):
        super().__init__(shape, undobuffersize, visible)
        self.speed(0)

    # Method to draw a heart
    def heart(self, center_x, center_y, size=20, colors="pink"):
        self.penup()
        self.setposition(center_x, center_y)
        self.pendown()
        self.begin_fill()
        self.color(colors)

        self.left(140)
        self.forward(size)
        for _ in range(200):
            self.right(1)
            self.forward(size * 0.0175)
        self.left(120)
        for _ in range(200):
            self.right(1)
            self.forward(size * 0.0175)
        self.forward(size* 2) 
        
        self.end_fill()
        self.penup()
        self.setheading(0)  # Reset direction

window = turtle.Screen()
window.setup(width=800, height=800)

# Create an instance of Turtle_Extended
t = Turtle_Extended()

colors =["purple", "blue", "pink", "red"]

# Draw hearts at the specified locations
hearts = [(-75, 0, 50),
    (0, 0, 100), # first complete heart 
    (-75, 75, 50),
    (-75, -75, 50),
    (0, 0, 50),
    (0, 75, 50),
    (0, -75, 50),
    (75, 0, 50),
    (75, 75, 50),
    (75, -75, 50),
    (0, 0, 250)]

# Draw hearts with different colors
for i, (x, y, size) in enumerate(hearts):
    t.heart(x, y, size, colors[i % len(colors)])

turtle.mainloop()
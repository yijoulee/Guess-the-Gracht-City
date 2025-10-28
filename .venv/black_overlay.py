from turtle import Turtle


class Black_overlay(Turtle):
    def __init__(self):
        super().__init__()
        self.stamps = {}  # Store position: stamp_id pairs
        self.createoverlay()

    def createoverlay(self):
        """Sets up an initial black overlay with a grid of stamps."""
        self.shape("square")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(-300, -300)

        # Create overlay stamps across the grid
        y = -300
        for __ in range(21):  # Number of rows
            for _ in range(21):  # Number of columns
                stamp_id = self.stamp()
                # Store each stamp ID with its position in the grid
                self.stamps[(self.xcor(), self.ycor())] = stamp_id
                self.forward(30)
            y += 30
            self.goto(-300, y)

    def clear_area(self, x, y):
        """Clears a stamp in the overlay at the nearest grid position."""
        # Snap x and y coordinates to the overlay's 20x20 grid
        grid_x = round(x / 30) * 30
        grid_y = round(y / 30) * 30

        # Clear the overlay stamp if it exists at the calculated grid position
        if (grid_x, grid_y) in self.stamps:
            self.clearstamp(self.stamps[(grid_x, grid_y)])
            del self.stamps[(grid_x, grid_y)]

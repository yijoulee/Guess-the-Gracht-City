from turtle import Turtle

LENGTH = 3
lichaamslengte = range(0, LENGTH)
x = 0
START_POSITIONS = []
for seg in lichaamslengte:
    START_POSITIONS.append(x)
    x -= 30
MOVING_DISTANCE = 20

class Snake:
    def __init__(self):
        self.lichaam_lijst = []
        self.createsnake()
        self.head = self.lichaam_lijst[0]

    def createsnake(self):
        for slang in START_POSITIONS:
            position = (slang, 0)
            self.add_seg(position = (slang, 0))

    def add_seg(self, position):
        slang_name = Turtle("square")
        slang_name.shapesize(stretch_len=1.5, stretch_wid=1.5)
        slang_name.color("white")
        slang_name.penup()
        slang_name.goto(position)
        self.lichaam_lijst.append(slang_name)

    def reset(self):
        for seg in self.lichaam_lijst:
            seg.goto(1000,1000)
        self.lichaam_lijst.clear()
        self.createsnake()
        self.head = self.lichaam_lijst[0]

    def extend(self):
        self.add_seg(self.lichaam_lijst[-1].position())
        self.move()

    def move(self):
        for seg in range(len(self.lichaam_lijst)-1, 0, -1):
            new_x = self.lichaam_lijst[seg - 1].xcor()
            new_y = self.lichaam_lijst[seg - 1].ycor()
            self.lichaam_lijst[seg].goto(new_x, new_y)
        self.lichaam_lijst[0].forward(MOVING_DISTANCE)

    def turn_left(self):
        if self.lichaam_lijst[0].heading() != 0:
            self.lichaam_lijst[0].setheading(180)

    def turn_right(self):
        if self.lichaam_lijst[0].heading() != 180:
            self.lichaam_lijst[0].setheading(0)

    def turn_up(self):
        if self.lichaam_lijst[0].heading() != 270:
            self.lichaam_lijst[0].setheading(90)

    def turn_down(self):
        if self.lichaam_lijst[0].heading() != 90:
            self.lichaam_lijst[0].setheading(270)
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-10, 0), (-20, 0), (-30, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)



    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.turtlesize(0.5)
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        for i in range(5):
            self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if int(self.head.heading()) != DOWN:
            self.head.setheading(UP)

    def down(self):
        if int(self.head.heading()) != UP:
            self.head.setheading(DOWN)

    def right(self):
        if int(self.head.heading()) != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if int(self.head.heading()) != RIGHT:
            self.head.setheading(LEFT)


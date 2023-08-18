from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.setheading(270)
        self.backward(BACKWARDS_MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(FORWARD_MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.backward(BACKWARDS_MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True




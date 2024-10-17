from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(position)




    def up(self):

        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x,new_y)

    def down(self,x= None):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x,new_y)

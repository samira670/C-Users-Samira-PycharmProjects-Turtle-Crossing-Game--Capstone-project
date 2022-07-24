from turtle import Turtle
#Timmy is our cute Turtle that wants to cross, please help him.
class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()

        self.goto(0, -280)
        self.setheading(90)



    def move(self):
        self.forward(20)

from turtle import Turtle
import random
colors = ["black", "red", "green", "blue", "purple", "pink", "yellow"]
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.penup()

        self.shape("square")
        self.shapesize(1,2)
        self.speed("slowest")


    def move(self):

        self.backward(100)




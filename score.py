from turtle import Turtle
#Timmy is our cute Turtle that wants to cross, please help him.
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(50, 250)
        self.i = 0
        self.scoreplus()




    def gameover(self):
         self.goto(0,0)
         self.write("Game is Over", font=('Arial',16 , 'normal'))

    def scoreplus(self):

        self.clear()

        self.write(f"Score = {self.i} & level = {self.i+1}", font=('Arial', 16, 'normal'))
        self.i+=1


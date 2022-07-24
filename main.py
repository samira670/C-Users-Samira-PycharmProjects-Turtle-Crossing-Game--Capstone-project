# This is a really fun Game that you should control your cute turtle to not hit the cars and If you can reach
#the end of the screen you level up and get score and the speed of cars will increase this game has 10 levels let's
#try it


#This is our fun Turtle timmy
from turtle_ import Timmy
from turtle import Screen
from car import Car
from score import Score
import time
import random





screen = Screen()
#We tur off our screen to see the game continously when update it
screen.tracer(0)

score = Score()


screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing Game")

timmy = Timmy()
screen.listen()
screen.onkey(timmy.move, "Up")


speed =["slow", "normal", "fast", "fastest"]
difficulty_level=0


game_is_on = True
game = True

cars = []
sleep = [1, 0.9, 0.8, 0.7, 0.5, 0.4, 0.3, 0.2, 0.1]
while game :
  car= Car()
  car.goto(320, random.randint(-280, 280))
  #decrease the time of sleeping in each level to increase the difficulty
  time.sleep(sleep[difficulty_level])
  screen.update()
  cars.append(car)
  for car_ in cars:
    car_.move()
    #if the distance of our turtle is less than 20 picels we will lose the game.
    if timmy.distance(car_.xcor(), car_.ycor())<20:
      print("You lose the Game")
      game = False
      score.gameover()

    #If our turtle be successful to go to the top of our screen it levels up
    if timmy.ycor()>300:

      timmy= Timmy()
      score.scoreplus()
      #Increase the car speed to increase the difficulty
      car.speed(speed[difficulty_level])

      screen.listen()
      screen.onkey(timmy.move, "Up")
      difficulty_level+=1




















screen.exitonclick()
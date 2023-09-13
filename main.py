import turtle as t
from snake import Snake
from food import Food
from score_board import Scoreboard
import time


screen = t.Screen()
screen.title("Yılan oyunu xD")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 11:
        food.refresh()
        score.add_Score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()


    #Detect collision with tail
    """
    for seg in snake.segments:
        if snake.head.distance(seg) < 5 and seg != snake.segments[0]:
            game_is_on = False
            score.game_over()
    """
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 5:
            score.reset()
            snake.reset()




screen.exitonclick()

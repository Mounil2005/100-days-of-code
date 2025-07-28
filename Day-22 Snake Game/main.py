import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0


win = turtle.Screen()
win.title("Snake Game 🐍")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)


head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"


segments = []

for i in range(1, 3):  
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("light green")
    segment.penup()
    segment.goto(head.xcor() - (20 * i), head.ycor())  
    segments.append(segment)


food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")


try:
    while True:
        win.update()

       
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.hideturtle()
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

            
            for i in range(1, 3):
                segment = turtle.Turtle()
                segment.shape("square")
                segment.color("light green")
                segment.penup()
                segment.goto(head.xcor() - (20 * i), head.ycor())
                segments.append(segment)

        
        if head.distance(food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color("light green")
            new_segment.penup()
            segments.append(new_segment)

            
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

            delay *= 0.98

        
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)
        if segments:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # Collision with self
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.hideturtle()
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

                
                for i in range(1, 3):
                    segment = turtle.Turtle()
                    segment.shape("square")
                    segment.color("light green")
                    segment.penup()
                    segment.goto(head.xcor() - (20 * i), head.ycor())
                    segments.append(segment)

        time.sleep(delay)

except turtle.Terminator:
    print("Game closed.")

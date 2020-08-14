import turtle

#screen
w = turtle.Screen()
w.title("Pong")
w.bgcolor("black")
w.setup(height=600,width=800)
w.tracer(0)


#scores
score_a = 0
score_b = 0


#paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.penup()
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color("white")
paddle_a.goto(-350, 0)


#paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.penup()
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color("white")
paddle_b.goto(350, 0)


#ball

ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("white")
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: 0 | player B: 0",align = "center", font=("Courier", 20, "normal"))



#moving paddles

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_dn():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_dn():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#keyboard listener


w.listen()
w.onkeypress(paddle_a_up, "w")
w.onkeypress(paddle_a_dn, "s")
w.onkeypress(paddle_b_up, "Up")
w.onkeypress(paddle_b_dn, "Down")

#main loop
while True:
    w.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} | player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} | player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    #stoping with paddles

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1



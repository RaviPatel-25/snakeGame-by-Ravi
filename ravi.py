import turtle
from turtle import*
import time
import random
import tkinter
from tkinter import*
wn=turtle.Screen()
wn.title("Snake game by CODING VODING")
t=turtle.Turtle()
wn.setup(height=1620,width=1028,startx=0,starty=0)
wn.tracer(0)
wn.bgcolor("chartreuse2")

#create a border

t.speed(0)
t.pensize(4)
t.up()
t.goto(-505,805)
t.down()
t.fd(1010)
t.rt(90)
t.fd(1010)
t.rt(90)
t.fd(1010)
t.rt(90)
t.fd(1010)

#score
score=0
delay=0.1

#snake
snake=turtle.Turtle()
snake.shapesize(1.5)
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.up()
snake.goto(0,0)
snake.direction='stop'

#food
fruit=turtle.Turtle()
fruit.shapesize(1.5)
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.up()
fruit.goto(30,30)

old_fruit=[]

#scoring
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.up()
scoring.ht()
scoring.goto(-370,-270)
scoring.write("Score :",align="center",font=("Courier",10,"bold"))

#move
def snake_go_up():
	if snake.direction != "down":
		snake.direction = "up"
		
def snake_go_down():
	if snake.direction != "up":
		snake.direction = "down"
		
def snake_go_left():
	if snake.direction != "right":
		snake.direction = "left"
		
def snake_go_right():
	if snake.direction != "left":
		snake.direction = "right"
		
def snake_move():
		if snake.direction == "up":
			y = snake.ycor()
			snake.sety(y+20)
			
		if snake.direction == "down":
			y = snake.ycor()
			snake.sety(y-20)
			
		if snake.direction == "left":
			x = snake.xcor()
			snake.setx(x-20)
			
		if snake.direction == "right":
			x = snake.xcor()
			snake.setx(x+20)
			
#keys
canvas=wn.getcanvas()
button=Button(canvas.master,text="Up",bd=15,bg='aqua',command=snake_go_up).place(x=450,y=1050,height=150,width=150)
button=Button(canvas.master,text="Down",bd=15,bg='aqua',command=snake_go_down).place(x=450,y=1350,height=150,width=150)
button=Button(canvas.master,text="Left",bd=15,bg='aqua',command=snake_go_left).place(x=310,y=1200,height=150,width=150)
button=Button(canvas.master,text="Right",bd=15,bg='aqua',command=snake_go_right).place(x=590,y=1200,height=150,width=150)


#mainloop
run=True
while run:
	wn.update()
	#snake and fruit codide
	if snake.distance(fruit)<20:
		 x=random.randint(-474,454)
		 y=random.randint(-210,800)
		 fruit.goto(x,y)
		 scoring.clear()
		 score+=1
		 scoring.write("Score :{}".format(score),align="center",font=("Courier",10,"bold"))
		 #delay-=0.001
	
		 
		 #new ball
		 new_fruit=turtle.Turtle()
		 new_fruit.shapesize(1.5)
		 new_fruit.speed(0)
		 new_fruit.shape("square")
		 new_fruit.color("red")
		 new_fruit.up()
		 old_fruit.append(new_fruit)
		 
	#add ball to snake
	for index in range(len(old_fruit)-1,0,-1):
		 a=old_fruit[index-1].xcor()
		 b=old_fruit[index-1].ycor()
		 
		 old_fruit[index].goto(a,b)
		 
	if len(old_fruit)>0:
		 a=snake.xcor()
		 b=snake.ycor()
		 old_fruit[0].goto(a,b)
		 
	snake_move()
	
	#snake border collision
	if snake.xcor()>480 or snake.xcor()<-483 or snake.ycor()>790 or snake.ycor()<-190:
		 time.sleep(1)
		 wn.clear()
		 wn.bgcolor("chartreuse2")
		 scoring.goto(0,0)
		 scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",15,"bold"))
	time.sleep(delay)
		 
t.Terminator()

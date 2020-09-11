import turtle

def o(x,y):
	turtle.goto(x,y)
	turtle.pendown()
	turtle.circle(50)
	turtle.penup()

def l(x,y):
	turtle.goto(x,y)
	turtle.pendown()
	turtle.goto(x,y-100)
	turtle.penup()

def nieun(x,y):
	turtle.goto(x,y)
	turtle.pendown()
	turtle.goto(x,y-100)
	turtle.goto(x+100,y-100)
	turtle.penup()

def gieok(x,y):
	turtle.goto(x,y)
	turtle.pendown()
	turtle.goto(x+100,y)
	turtle.goto(x+100,y-100)
	turtle.penup()

def siot(x,y):
	turtle.goto(x,y)
	turtle.pendown()
	turtle.goto(x-40,y+100)
	turtle.goto(x-80,y)
	turtle.penup()

turtle.penup()

gieok(-400,100)
l(-200,100)
gieok(-300,-100)
nieun(-300,-100)

siot(0,0)
gieok(-100,-100)

nieun(100,200)
o(150,0)
nieun(250,100)
nieun(150,-100)

turtle.exitonclick()

import turtle

count = 6
while (count>0):
    turtle.forward(300)
    turtle.backward(300)
    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()
    turtle.right(90)
    count = count-1
turtle.penup()
turtle.right(90)
turtle.forward(60)
turtle.pendown()

count = 6
while(count>0):
    turtle.forward(300)
    turtle.backward(300)
    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()
    turtle.right(90)
    count = count-1
    
turtle.exitonclick()

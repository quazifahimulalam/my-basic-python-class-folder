import turtle

turtle.screensize(600,600)
turtle.bgcolor("black")

p = turtle.Turtle()
n = 6
p.pensize(7)
p.color("white")
p.shape("turtle")
for i in range(n):
    p.forward(100)
    p.left(360/n)
    
for i in range(n):
    p.forward(100)
    p.right(360/n)
    

    
turtle.done()

import turtle

turtle.screensize(600,600)
turtle.bgcolor("cornflowerblue")

p = turtle.Turtle()
p.pensize(7)
p.color("white")
p.shape("turtle")

p.penup()
p.goto(0,100)
p.pendown()

for _ in range(5):
    p.forward(200)
    p.right(144)
    

p.penup()
p.goto(0,-100)
p.pendown()

for _ in range(5):
    p.forward(200)
    p.right(144)
    
    
p.penup()
p.goto(-300,100)
p.pendown()

for _ in range(5):
    p.forward(200)
    p.right(144)
    
p.penup()
p.goto(-300,-100)
p.pendown()

for _ in range(5):
    p.forward(200)
    p.right(144)
    

    
turtle.done()
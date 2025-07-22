import turtle
import colorsys

def draw_flower():
    # Set up screen
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Create turtle
    flower = turtle.Turtle()
    flower.speed(0)
    flower.width(2)

    # Define colors using HSV to get a rainbow effect
    n = 36  # Number of petals
    hue = 0  # Starting hue

    for i in range(360):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        flower.color(color)
        flower.forward(200)
        flower.left(45)
        flower.forward(200)
        flower.left(170)  # Petal loop
        hue += 1/n  # Increment hue for color variation
        flower.left(1)

    # Draw center of the flower
    flower.penup()
    flower.goto(0, -20)
    flower.pendown()
    flower.color("yellow")
    flower.begin_fill()
    flower.circle(20)
    flower.end_fill()

    # Hide turtle and display the window
    flower.hideturtle()
    turtle.done()

# Run the function
draw_flower()

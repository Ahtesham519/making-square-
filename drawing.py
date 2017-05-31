import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # create the turtle Brad - Draw a square

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("Yellow")
    brad.speed(4)
    draw_square(brad)
    for i in range(1,20):
        draw_square(brad)
        brad.right(240)

    #Create the turtle angle - Draw a circle
    #angle = turtle.Turtle()
    #angle.shape("arrow")
    #angle.color("Black")
    #angle.circle(100)

    window.exitonclick()

draw_art()

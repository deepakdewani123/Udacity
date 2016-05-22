import turtle

def my_name():
    
    window = turtle.Screen()
    window.bgcolor("#FF2A68")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("#FFCC00")
    brad.speed(8)

    brad.right(90)
    brad.forward(200)
    brad.right(-90)
    brad.circle(100,180)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.speed(8)
    
    angie.pos(100,100)
    angie.right(90)
    angie.forward(100)


def triangle(turtle):
    for i in range(1,4):
        turtle.right(30)
        turtle.forward(100)
        turtle.right(90)
        
def flower():
    window = turtle.Screen()
    window.bgcolor("#FF2A68")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("#FFCC00")
    brad.speed(0)

    for i in range(1,37):
        triangle(brad)
        brad.right(10)
        
    brad.right(90)
    brad.forward(200)

flower()
    

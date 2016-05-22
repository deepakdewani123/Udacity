import turtle

def square(turtle):
  for i in range(1,5):
      turtle.forward(100)
      turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("yellow")
    brad.speed(8)
    
    for i in range(1,37):
        square(brad)
        brad.right(10)
        
draw_art()


def circle():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(15)
    brad.circle(100)


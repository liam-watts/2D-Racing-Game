from turtle import Screen, Turtle

#parameters
TURTLE_SIZE = 20
boundary = 400
speed = 5

# functions
def go_left():
    car.direction = 'left'

def go_right():
    car.direction = 'right'

# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Racing Cars")
screen.bgcolor('white')
screen.tracer(0)

# Adding the car
car = Turtle()
car.shape('turtle')
car.speed('fastest')
car.color('blue')
car.penup()
car.sety(-250)
car.direction = 'stop'

# Keyboard
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')
screen.listen()

while True:
    x = car.xcor()

    if car.direction == 'left':
        if x > TURTLE_SIZE - boundary:
            x -= speed
            car.setx(x)
        else:
            car.direction = 'stop'
    elif car.direction == 'right':
        if x < boundary- TURTLE_SIZE:
            x += speed
            car.setx(x)
        else:
            car.direction = 'stop'

    screen.update()

import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

########### Challenge 3 - Draw Shapes ########
import random


def draw_shape(angle):
    # color_no = randint(0,255)
    angle_degree = 360 / angle
    for _ in range(angle):
        tim.right(angle_degree)
        tim.forward(100)


def get_color():
    tim.getscreen().colormode(255)
    color_no = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    tim.pencolor(color_no)


for angle in range(3, 11):
    get_color()
    draw_shape(angle)

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

direct_num = random.randint(0, 1)
degree = [0, 90, 180, 270]


# can be replaced by setheading
def get_direction(direct_num):
    if direct_num == 1:
        tim.right(random.choice(degree))
    else:
        # tim.forward(random.randint(1,10))
        tim.left(random.choice(degree))
    tim.forward(random.randint(25, 50))


for _ in range(100):
    turtle_color = random.choice(colours)
    tim.color(turtle_color)
    tim.pensize(12)
    get_direction(direct_num)


########### Challenge 5 - Spirograph ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fast")
def draw_spirographh(size_degree):
    for degree in range(0, 360, size_degree):
        tim.color(random_color())
        tim.setheading(degree)
        tim.circle(50)

draw_spirographh(5)

from turtle import Screen,Turtle


# set up the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# body list
snake_body=[]


# set three turtles
for i in range(3):
  # set up the snake body
  square_body =Turtle()
  square_body.penup()
  square_body.shape("square")
  # square_body.shapesize(stretch_wid=2,stretch_len=2)
  square_body.color("white")
  square_body.goto(-i*20,0)
  snake_body.append(square_body)
  print(square_body.pos())
  



screen.exitonclick()

import turtle as t
import random
my_graph = t.Turtle()
color_list = [(240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124),
              (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35),
              (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50),
              (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

'''
10 x 10 rows
20 - 50(distance) - 20(size of dot)
'''
t.colormode(255)

def draw_line():
  for line in range(10):
    color = random.choice(color_list)
    my_graph.dot(20,color)
    my_graph.forward(50)

# (0,50) ->(50,50) ->(100,50)
# (0,0) ->(50,0) -> (100,0)
for row in range(10):
  my_graph.penup()
  my_graph.hideturtle()
  num_x = -200
  num_y = -200 + row * 50
  my_graph.setposition(num_x,num_y)
  draw_line()

import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
turtle.colormode(255)

#import colorgram

#damien_colors = colorgram.extract('image.jpg', 30)

#print(damien_colors)

#rgb_colors = []

#for color in damien_colors:
 #   r = color.rgb[0]
 #   #or color.rgb.r
 #   g = color.rgb[1]
 #   b = color.rgb[2]
 #   rgb_colors.append((r, g, b))

#print(rgb_colors)

color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

turtle.home()
#screen.setup(width=600, height=600)
turtle.setworldcoordinates(-50,-50, 500, 500)

def draw_dotline():
    for _ in range(9):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.dot(20, random.choice(color_list))

def goto_next_linestart():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(450)
    tim.left(180)

for _ in range(10):
    tim.hideturtle()
    tim.pu()
    draw_dotline()
    goto_next_linestart()






screen.exitonclick()
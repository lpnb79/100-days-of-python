import turtle as t
import random
#import colorgram

#colors = colorgram.extract('day18\\image.jpg', 20)
#rgb = []
#
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb.append(new_color)

color_list = [
    (206, 78, 6), (8, 12, 48), (105, 192, 177), (228, 39, 65), (171, 192, 6), (216, 226, 219), (186, 134, 121), (133, 157, 187), (63, 105, 125), (175, 2, 119), (59, 171, 4), (24, 84, 64), (120, 96, 1), (228, 201, 3), (3, 25, 128), (191, 45, 68), (188, 128, 135)
              ]

t.colormode(255)

tim = t.Turtle()
tim.ht()
#tim.shape("classic")
tim.speed(0)
tim.teleport(-200.00, -200.00)

def draw_dot(color):
    tim.fillcolor(color)
    with tim.fill():
        tim.circle(10)

def move_right():
    tim.pu()
    tim.fd(50)
    tim.pd()

def draw_row():
    for i in range(10):
        rand_color = random.choice(color_list)
        tim.color(rand_color)
        draw_dot(rand_color)
        move_right()

for i in range(1, 11):
    draw_row()
    tim.teleport(-200.00, -200.00 + (i * 50))



screen = t.Screen()
screen.exitonclick()














###########################################################################################
#turtle_colors = [
#    # Vibrant & Rainbow
#    "red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta",
#    # Bright & Neon
#    "lime", "pink", "deepskyblue", "hotpink", "chartreuse", "springgreen", "gold", "aqua",
#    # Pastels & Soft Tones
#    "peachpuff", "lightpink", "powderblue", "palegreen", "lavender", "mistyrose", "khaki", "plum",
#    # Deep & Dark Tones
#    "navy", "darkgreen", "crimson", "indigo", "maroon", "darkslategray", "midnightblue", "darkgoldenrod",
#    # Earthy & Natural
#    "coral", "teal", "turquoise", "chocolate", "sienna", "olivedrab", "sandybrown", "salmon",
#    # Grays & Neutrals
#    "black", "gray", "darkgray", "lightgray", "slategray", "gainsboro", "bisque"
#]
#
#def random_color():
#    r = random.randint(0,255)
#    g = random.randint(0,255)
#    b = random.randint(0,255)
#    color = (r, g, b) 
#    return color
#
#DRAW 3 TO 10 SIDED 
#def draw_shapes(num_sides):
#    angle = (360 / num_sides) 
#    for i in range(num_sides):
#        tim.fd(100)
#        tim.right(angle)
#
#for i in range(3, 11):
#    tim.pensize(3)
#    tim.color(random.choice(turtle_colors))
#    draw_shapes(i)

#RANDOM WALK
#tim.pensize(10)
#turn = [0, 90, 180, 270]
#for i in range(100):
#    tim.speed(10)
#    tim.color(random.choice(turtle_colors))
#    tim.seth(random.choice(turn))
#    tim.fd(25) 

#RANDOM WALK WITH COLOR GENERATOR USING RBG
#turn = [0, 90, 180, 270]
#for i in range(200):
#    tim.pensize(12)
#    tim.speed(0)
#    tim.color(random_color())
#    tim.seth(random.choice(turn))
#    tim.fd(25) 

#MAKE A SPIROGRAPH
#for i in range(0, 361, 4):
#    tim.setheading(i)
#    tim.circle(100)
#    tim.color(random_color())

#alternative way according to lecture
#def spirograph(gap_size):
#    for i in range(int(360 / gap_size)):
#        tim.color(random_color())
#        tim.circle(100)
#        tim.setheading(tim.heading() + gap_size)
#
#spirograph(5)
    

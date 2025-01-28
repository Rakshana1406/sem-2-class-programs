
#using loop
import turtle

star=turtle.Turtle()
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)


#without using loop
import turtle

s=turtle.Turtle()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)



# pen up & pen down
import turtle

s=turtle.Turtle()
s.forward(100)
s.penup()
s.right(90)
s.forward(100)
s.right(90)
s.pendown()
s.forward(100)

# filling colors
 # for star
import turtle

star=turtle.Turtle()
star.color("green","orange")
star.begin_fill()
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

star.end_fill()

 #for square
s=turtle.Turtle()
s.color("blue","pink")
s.begin_fill()
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)
s.left(90)
s.forward(100)

s.end_fill()

 #for heart shape with hide turtle

import turtle

s=turtle.Turtle()

s.fillcolor("red")
s.begin_fill()
s.right(45)
s.forward(100)
s.left(90)
s.forward(100)
s.circle(50,180)
s.right(90)
s.circle(50,180)
s.end_fill()
s.hideturtle()




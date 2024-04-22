from turtle import *

# we want to paint a house

# step 1: draw a square
shape("circle")
speed(5)
width(7)
color("orange")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
# end of square

# drawing a door
begin_fill()
forward(70)
left(90)
color("brown")
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
# end of the door
penup()
goto(200,200) 
pendown()



color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing the windows
penup()
goto(50,100)
pendown()

color("light blue")
left(210)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)

penup()
goto(150,100)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25) 
right(90)
forward(50)


        

exitonclick()
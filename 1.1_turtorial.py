'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
tyson=turtle.Turtle()
tyson.penup()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('white') # colors the screen
tyson.pensize(3) # width of pen line
tyson.speed(10)  # speed of drawing. Go fast to not waste time.
tyson.color('black')
#creating the vial
tyson.goto(0,100)
tyson.down()
tyson.goto(20,100)
tyson.goto(0,100)
tyson.goto(-20,100)
tyson.goto(-20,-100)
tyson.penup()
tyson.goto(20,100)
tyson.down()
tyson.goto(20,-100)
tyson.penup()
tyson.goto(-20,-100)
tyson.down()
tyson.right(90)
tyson.circle(20,180)
#filling vial attempt now
tyson.penup()
tyson.color('#00FF00')
tyson.goto(-17,-100)
tyson.left(180)
tyson.down()
tyson.begin_fill()
tyson.circle(17,180)
tyson.end_fill()
#ok cool bottom is filled
#now make a loop to fill in the rest going horizontally because i cant use fill
tyson.goto(-17,-100)
tyson.right(90)

times = 90
for x in range(90):
    tyson.forward(34)
    tyson.left(90)
    tyson.forward(1)
    tyson.left(90)
    tyson.forward(34)
    tyson.right(90)
    tyson.forward(1)
    tyson.right(90)


#idea: add air bubbles that are random every time
#maybe use an rng does that exist in python
#nvm that would require me to code that they also dont interlap aint nobody got time for that

#adding non random bubbles now
tyson.penup()
tyson.color('white')
tyson.goto(-10,69)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

tyson.penup()
tyson.color('white')
tyson.goto(-5,-110)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

tyson.penup()
tyson.color('white')
tyson.goto(6,40)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

tyson.penup()
tyson.color('white')
tyson.goto(1,0)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

tyson.penup()
tyson.color('white')
tyson.goto(12,-90)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

tyson.penup()
tyson.color('white')
tyson.goto(-3,-50)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

tyson.penup()
tyson.color('white')
tyson.goto(-8,10)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

#now green bubbles for a final touch
tyson.penup()
tyson.color('#00FF00')
tyson.goto(-8,120)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

tyson.penup()
tyson.color('#00FF00')
tyson.goto(12,130)
tyson.pendown()
tyson.begin_fill()
tyson.circle(3)
tyson.end_fill()

#make it into a smiley face for fun aint nothing wrong with that

tyson.penup()
tyson.goto(-2,107)
tyson.pendown()
tyson.circle(35,60)

tyson.penup()
tyson.setpos(200,-300)
tyson.down()
tyson.pencolor('black')


tyson.write('Lindy Huynh',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing

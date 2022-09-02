'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
tyson=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
tyson.pensize(3) # width of pen line
tyson.speed(10)  # speed of drawing. Go fast to not waste time.
tyson.color("#ffffff")
tyson.home()
tyson.circle(50)



tyson.penup()
tyson.setpos(200,-300)
tyson.down()
tyson.pencolor('#ffffff')


tyson.write('Lindy Huynh',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing

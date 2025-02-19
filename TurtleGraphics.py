#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8)

    side_length = 50
    num_sides = 8
    myTurtle.forward(50)
    angle = 360 / num_sides  
    for i in range(num_sides) : 
        myTurtle.forward(side_length)
        myTurtle.right(angle)
        
    
    side_length = 50
    num_sides = 5
    myTurtle.forward(50)
    angle = 360 / num_sides
    for i in range(num_sides) : 
      myTurtle.forward(50)
      myTurtle.right(angle)
      
    

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    
    side_length = 200
    myTurtle.penup()
    myTurtle.goto(-100, -100)
    myTurtle.pendown()
    for _ in range(4):
        myTurtle.forward(side_length)
        myTurtle.left(90)

    myTurtle.penup()
    myTurtle.goto(0, 100)
    myTurtle.pendown()
    myTurtle.begin_fill()
    myTurtle.forward(100)  
    myTurtle.right(90)    
    myTurtle.forward(100)  
    myTurtle.right(90)    
    myTurtle.forward(100)  
    myTurtle.right(90)    
    myTurtle.forward(100)  
    myTurtle.end_fill()
    
    



    

main()

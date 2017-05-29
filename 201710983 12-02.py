import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquareAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)
def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range(0,3):
        t1.forward(size)
        t1.right(120)
def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    for i in range(0,5):
	t1.forward(size)
	t1.right(180-36)

drawSquareAt(0,0,100)
drawTriangleAt(200,200,100)
drawStarAt(500,500,100)
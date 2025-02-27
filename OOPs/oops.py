# from turtle import * 

# t = Turtle()
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)

# # Keep the window open
# # done()
# mainloop()  # Keeps the turtle window open

# from turtle import *

# t = Turtle()
# t.width(5)
# t.color('orange')

# for i in range(6):
#     t.forward(100)
#     t.left(60)
    
# exitonclick()  # Closes the turtle window when clicked    
from turtle import *

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.width(5)
t2.width(5)
t3.width(5)

t1.color('orange')
t2.color('blue')
t3.color('green')

t1.penup()
t2.penup()
t3.penup()

t1.goto(-150,-150)
t2.goto(-150,50)
t3.goto(-150,-50)

t1.pendown()
t2.pendown()
t3.pendown()

t1.begin_fill()
t2.begin_fill()
t3.begin_fill()

for i in range(3):
    t1.forward(100)
    t1.left(120)
    
    t2.forward(100)
    t2.left(120)
    
    t3.forward(100)
    t3.left(120)
    
t1.end_fill()
t2.end_fill()
t3.end_fill()

exitonclick()  # Closes the turtle window when clicked    

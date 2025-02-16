from turtle import *

# pencil = Turtle()

# colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange'] 

# for i in range(6):
#     pencil.color(colors[i])
#     pencil.width(5)
#     pencil.forward(100)
#     pencil.right(60)
    
# exitonclick()    

pencil = Turtle()

def square(p, size , color):
    p.color(color)
    p.begin_fill()
    for i in range(4):
        p.forward(size)
        p.right(90)
    p.end_fill()
    
def pentagon(p, size , color):
    p.color(color)
    p.begin_fill()
    for i in range(5):
        p.forward(size)
        p.right(72)
    p.end_fill()
    
start = input("square/circle/pentagon :").lower()    

while start != "stop":
    if start == "square":
        square(pencil, 100, "red")
        size = int(input("Enter the size: "))
        color = input("Enter the color: ")
        square(pencil, size, color)
        
    elif start == "circle":
        radius = int(input("Enter the radius: "))   
        color = input("Enter the color: ")
        circle(pencil, radius, color)
    
    elif start == "pentagon":
        size = int(input("Enter the size: "))   
        color = input("Enter the color: ")
        pentagon(pencil, size, color)
    else:
        print("Invalid input")            
    
    start = input("square/circle/pentagon :").lower() 
    
exitonclick() 
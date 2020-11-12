import turtle
turtle.reset()

fill = 0  # переключатель заливки

for y in range (0 , 320, 40):

    if fill == 0:
        fill = 1
        turtle.color("black", "red") # цвет пера , цвет заливки        
    else:
        fill = 0
        turtle.color("black", "white")
    
    for x in range (0 , 320, 40):
        
        turtle.goto(x,y)  # Рисует квадрат
        turtle.down()
        turtle.begin_fill()
        turtle.forward(40) 
        turtle.right(90)   
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.end_fill()
        turtle.up()
        
        if fill == 0:
            fill = 1
            turtle.color("black", "red")           
        else:
            fill = 0
            turtle.color("black", "white")

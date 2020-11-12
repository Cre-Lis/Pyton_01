import turtle
turtle.reset()

def draw_square(a, pen, brush):  # Рисует квадрат сторона, перо, кисть

    turtle.color(pen, brush) # цвет пера , цвет заливки
    turtle.down();
    turtle.begin_fill();
    turtle.forward(a); 
    turtle.right(90);   
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

fill = 0       # переключатель типа заливки
Pen = "black"  # цвет пера


for y in range (0 , 320, 40):

    if fill == 0:
        fill = 1
        Brush = "red"
    else:
        fill = 0
        Brush = "white"
    
    for x in range (0 , 320, 40):
        
        turtle.goto(x,y)  
        draw_square(30, Pen, Brush)  # Рисует квадрат сторона, перо, кисть
        
        if fill == 0:
            fill = 1
            Brush = "red"
        else:
            fill = 0
            Brush = "white"





    
    

import turtle
turtle.reset()
turtle.speed(0)
turtle.hideturtle()


def draw_square(a):  # Рисует квадрат сторона   
    #turtle.down()
    turtle.forward(a) 
    turtle.right(90)   
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    #turtle.up()

    
for y in range (360):
    draw_square(200)
    turtle.right(1)

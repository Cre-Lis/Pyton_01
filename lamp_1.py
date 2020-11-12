import time



import turtle
turtle.reset()
turtle.speed(0)
turtle.hideturtle()

turtle.up()
turtle.goto(0,250)  
turtle.down()
turtle.write("СВЕТОФОР", align = "center", font = ("Arial", 30, "normal"))


turtle.up()
turtle.goto(0,120)  
turtle.down()

while (1):
    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.circle(50,360,360)
    turtle.end_fill()
    time.sleep(2) # засыпаем на 2 секунды  

    turtle.color("black", "red") # цвет пера , цвет заливки            
    turtle.begin_fill()
    turtle.circle(50,360,360)
    turtle.end_fill()
    time.sleep(2) # засыпаем на 2 секунды

    turtle.up()
    turtle.goto(0,0)  
    turtle.down()

    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.circle(50,360,360)
    turtle.end_fill()
    time.sleep(2) # засыпаем на 2 секунды  

    turtle.color("black", "yellow") # цвет пера , цвет заливки            
    turtle.begin_fill()
    turtle.circle(50,360,360)
    turtle.end_fill()
    time.sleep(2) # засыпаем на 2 секунды

    turtle.up()
    turtle.goto(0,-120)  
    turtle.down()

    turtle.color("black", "white")
    turtle.begin_fill()
    turtle.circle(50,360,360)
    turtle.end_fill()
    time.sleep(2) # засыпаем на 2 секунды  

    turtle.color("black", "green") # цвет пера , цвет заливки            
    turtle.begin_fill()
    turtle.circle(50,360,360)
    turtle.end_fill()
    time.sleep(2) # засыпаем на 2 секунды

    turtle.up()
    turtle.goto(0,120)  
    turtle.down()










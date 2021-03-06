import tkinter as tk
import turtle


def koch(Distance, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch (Distance / 3, order - 1)
            turtle.left(t)
    else:
        turtle.forward(Distance)



def T():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-125 ,25)      #起始位置
    turtle.setheading(0)       #畫筆方向(0 東 90 北 180西 270南)

    
    turtle.clear()
    turtle.pendown()
    for i in range(3) :
        koch (150, int(Input1.get()))
        turtle.pencolor("#000000")
        turtle.left(-120)       #turtle.right() 裡面的值填的是角度


    

win = tk.Tk()
win.title("snowflake") #視窗名稱
win.geometry("600x650" )#視窗大小

canvas = tk.Canvas(win, width = 600, height = 600)
canvas.pack()
canvas.place(x = 0, y = 0)

turtle = turtle.RawTurtle(canvas)


Input1 = tk.Entry(win, width = 10,justify = "center")
Input1.pack() 


button = tk.Button(win, text = "START", command = T)
button.pack()
button.place(x = 275, y = 30)


win.mainloop()
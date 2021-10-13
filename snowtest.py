import tkinter as tk
import turtle
import random

def koch(Distance,order):
    if order > 0:
        for t in [60 ,-120, 60,0]:
            koch(Distance / 3, order -1)
            turtle.left(t)
    else:
        turtle.forward(Distance)


def T():
    canvas.delete("all")
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-125,25)    #起始位置
    turtle.setheading(0)    #畫筆方向(0 東 90 北 180西 270南)

    turtle.pendown()
    turtle.pencolor("#002742")
    for i in range(3):
        koch(150,int(Input1.get()))
        turtle.pencolor("#004474")
        turtle.left(-120)

    


win = tk.Tk()
win.title("snowflake")  #視窗名稱
win.geometry("600x650") #視窗大小

canvas = tk.Canvas(win,width = 600, height = 600) #畫布大小
canvas.pack()
canvas.place(x = 0,y = 50)

turtle = turtle.RawTurtle(canvas)

Input1 = tk.Entry(win, width = 10, justify = "center")
Input1.pack()

button = tk.Button(win, text = "START", command=T)
button.pack()
button.place(x = 275, y = 30)

win.mainloop()
import tkinter as tk
  
def change_Color():
    wrong_label.config(bg="red")

def count():
  try:
    h = float(height_input.get())
    w = float(weight_input.get())
  except:
    wrong.set("it’s not number!please enter number.")
    change_Color()
  h /= 100.0
  result.set("your BMI is " + str(w/h**2)) 

window = tk.Tk()
window.title('Demo用視窗')
window.geometry("400x200")

height = tk.Label(window,text="請輸入您的身高: ",fg="black",bg="pink")
height.pack()
height.place(x=0,y=10)

height_input = tk.Entry(window)
height_input.pack()
height_input.place(x=100,y=10)

weight = tk.Label(window,text="請輸入您的體重: ",fg="black",bg="pink")
weight.pack()
weight.place(x=0,y=40)

weight_input = tk.Entry(window)
weight_input.pack()
weight_input.place(x=100,y=40)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result,font=("標楷體",16))
result_label.pack()
result_label.place(x=0,y=100)

wrong = tk.StringVar()
wrong_label = tk.Label(window,textvariable=wrong)
wrong_label.pack()
wrong_label.place(x=0,y=70)

count_button = tk.Button(window, text="GO", command=count)
count_button.pack()
count_button.place(x=250,y=5)

close_button = tk.Button(window, text="Close", command=window.destroy)
close_button.pack()
close_button.place(x=250,y=35)

tk.mainloop()


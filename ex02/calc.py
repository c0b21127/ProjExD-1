print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(f"{txt}",f"{txt}のボタンが押されました")
    entry.insert(tk.END,txt)

def click_equal(event):
    equal = entry.get()
    result = eval(equal)
    entry.delete(0,tk.END)
    entry.insert(tk.END,result)
    
    

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root,width = 10,font=("Times New Roman", 30),justify="right")
entry.grid(row=0,column=0,columnspan=3)


r, c = 1, 0  #行、列を表示する変数
for i, num in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=3, height=1)
    btn.bind("<1>",button_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0


#プラスの追加
btn1 = tk.Button(root, text="+", font=("Times New Roman", 30), width=3, height=1)
btn1.grid(row = 3, column= 3 )
btn1.bind("<1>",button_click)

#イコールの追加
btn2 = tk.Button(root, text="=", font=("Times New Roman", 30), width=3, height=1)
btn2.grid(row = 4, column= 3)
btn2.bind("<1>",click_equal)

#00の追加
btn3 = tk.Button(root, text="00", font=("Times New Roman", 30), width=3, height=1)
btn3.grid(row = 4, column= 1)
btn3.bind("<1>",button_click)

#.の追加
btn4 = tk.Button(root, text=".", font=("Times New Roman", 30), width=3, height=1)
btn4.grid(row = 4, column= 2)
btn4.bind("<1>",button_click)

root.mainloop()
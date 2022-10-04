print("hello world")

import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(f"{txt}",f"{txt}のボタンが押されました")
    entry.insert(tk.END,txt)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root,width = 10,font=("Times New Roman", 30),justify="right")
entry.grid(row=0,column=0,columnspan=3)


r, c = 1, 0
for i, num in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=4, height=1)
    btn.bind("<1>",button_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

btn1 = tk.Button(root, text="+", font=("Times New Roman", 30), width=4, height=1)
btn1.grid(row = 4, column= 1 )
btn1.bind("<1>",button_click)
root.mainloop()
import tkinter as tk

import math


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(f"{txt}",f"{txt}のボタンが押されました")
    entry.insert(tk.END,txt)

# =を押したとき
def click_equal(event):
    equal = entry.get()
    result = eval(equal)
    entry.delete(0,tk.END)
    entry.insert(tk.END,result)

# ACを押したとき
def click_Alldelete(event):
    entry.delete(0,tk.END)

# Cを押したとき
def click_delete(event):
    delete = entry.get()
    entry.delete(len(delete)-1,tk.END)

# √を押したとき
def click_sqrt(event):
    sqrt = entry.get()
    result = math.sqrt(int(sqrt))
    entry.delete(0,tk.END)
    entry.insert(tk.END, result)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root,width = 10,font=("Times New Roman", 30),justify="right")
entry.grid(row=0,column=0,columnspan=3)


r, c = 2, 0  #行、列を表示する変数
for i, num in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=3, height=1)
    btn.bind("<1>",button_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

#足し算の追加
btn1 = tk.Button(root, text="+", font=("Times New Roman", 30), width=3, height=1)
btn1.grid(row = 4, column= 3 )
btn1.bind("<1>",button_click)

#イコールの追加
btn2 = tk.Button(root, text="=", font=("Times New Roman", 30), width=3, height=1)
btn2.grid(row = 5, column= 3)
btn2.bind("<1>",click_equal)

#00の追加
btn3 = tk.Button(root, text="00", font=("Times New Roman", 30), width=3, height=1)
btn3.grid(row = 5, column= 1)
btn3.bind("<1>",button_click)

#小数点.の追加
btn4 = tk.Button(root, text=".", font=("Times New Roman", 30), width=3, height=1)
btn4.grid(row = 5, column= 2)
btn4.bind("<1>",button_click)

#引き算の追加
btn5 = tk.Button(root, text="-", font=("Times New Roman", 30), width=3, height=1)
btn5.grid(row = 3, column= 3)
btn5.bind("<1>",button_click)

#掛け算の追加
btn6 = tk.Button(root, text="*", font=("Times New Roman", 30), width=3, height=1)
btn6.grid(row = 2, column= 3)
btn6.bind("<1>",button_click)

#割り算の追加
btn7 = tk.Button(root, text="/", font=("Times New Roman", 30), width=3, height=1)
btn7.grid(row = 1, column= 3)
btn7.bind("<1>",button_click)

#AllClearボタン追加
btn8 = tk.Button(root, text="AC", font=("Times New Roman", 30), width=3, height=1)
btn8.grid(row = 1, column= 0)
btn8.bind("<1>",click_Alldelete)

#Clearボタン追加
btn9 = tk.Button(root, text="C", font=("Times New Roman", 30), width=3, height=1)
btn9.grid(row = 1, column = 1)
btn9.bind("<1>",click_delete)

#平方の追加
btn10 = tk.Button(root, text="√", font=("Times New Roman", 30), width=3, height=1)
btn10.grid(row = 1, column = 2)
btn10.bind("<1>",click_sqrt)

root.mainloop()
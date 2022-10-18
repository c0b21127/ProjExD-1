import tkinter as tk
import maze_maker


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def start_back(event): #位置の初期化
    global mx, my
    mx , my = 1,1
    

def main_proc():
    global cx, cy
    global mx, my 
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1
    if maze_list[my][mx] ==0:
        cx, cy = mx*100 + 50, my*100 + 50   
    else: # 壁なら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori",cx, cy)   
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root,width = 1500,height = 900, bg= "black")
    canv.pack()

    maze_list = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canv,maze_list)
    
    tori = tk.PhotoImage(file="pika.png")
    cx, cy = 300, 400
    mx, my = 1,1
    canv.create_image(cx, cy, image=tori, tag = "tori")

    key = "" #グローバル変数keyは、現在押されているキーを表す変数である #練習4

    root.bind("<KeyPress>",key_down) #練習5

    root.bind("<KeyRelease>", key_up) #練習6

    root.bind("<1>", start_back) #スタートに戻る 

    main_proc()

    root.mainloop()
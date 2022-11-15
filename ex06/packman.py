from tkinter import font
import pygame 
import sys
from pygame.locals import *
import pygame as pg


WIDTH  = 440    # 画面横サイズ
HEIGHT = 280    # 画面縦サイズ
B_SIZE = 40   # 辺長
M_SIZE = 20   # 半径
M_DOT  = 40   # 移動ドット
W_TIME = 20   # 待ち時間
F_SIZE = 60   # フォントサイズ

class Screen:
    def __init__(self, title, wh,bgimg):
        pg.display.set_caption(title) #タイトル
        self.sfc = pg.display.set_mode(wh) #画面の大きさ(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #背景
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Text:# テキストを出力させるクラス

    def __init__(self,text,color,basyo):
        self.text = text
        self.color = color
        self.size = basyo
    
    def blit(self, scr:Screen):
        font = pg.font.Font(None,300)
        t = font.render(self.text, True, self.color)
        scr.sfc.blit(t, self.size)


####### 0 1 2 3 4 5 6 7 8 9 10  #####
MAP = [[1,1,1,1,1,1,1,1,1,1,1],   # 0
       [1,0,1,0,1,0,1,0,1,0,1],   # 1
       [1,1,1,1,1,1,1,1,1,1,1],   # 2
       [1,0,1,0,1,0,1,0,1,0,1],   # 3
       [1,1,1,1,1,1,1,1,1,1,1],   # 4
       [1,0,1,0,1,0,1,0,1,0,1],   # 5
       [1,1,1,1,1,1,1,1,1,1,2]]   # 6



def main():
    draw_maze()

    move_bomb()

    input_key()


def move_bomb(): # 動く敵
    ene =  pygame.image.load("fig/0.png")
    surface.blit(ene,(160,120))
    pygame.display.update()


def draw_maze():  #マップ表示
    ### 座標初期化
    x = 0
    y = 0

    for b1 in MAP:          # 1次元リスト
        for b2 in b1:       # 2次元リスト
            if   b2 == 0:   # 壁描画
                pygame.draw.rect(surface, (48, 48, 48), (x*B_SIZE,y*B_SIZE,B_SIZE,B_SIZE), 0)
            elif b2 == 1:   # 通路描画
                pygame.draw.rect(surface, (224,224,224), (x*B_SIZE,y*B_SIZE,B_SIZE,B_SIZE), 0)
            elif b2 == 2:   # ゴール描画
                pygame.draw.rect(surface, (0,0,255), (x*B_SIZE,y*B_SIZE,B_SIZE,B_SIZE), 0)
            x += 1
        ### 座標更新
        else:
            x = 0
            y += 1
    pygame.display.update()


def input_key(): # キャラの描画とキーの移動
 
    ### 座標初期化
    row = 0         # リスト縦
    col = 0         # リスト横
    now_x = M_SIZE  # 横座標
    now_y = M_SIZE  # 縦座標
    bak_x = M_SIZE  # 横前座標
    bak_y = M_SIZE  # 縦前座標
    e_flag = 0      # 終了フラグ
 
    ### イベント待ち
    while True:
 
        ### ゴール確認
        if MAP[row][col] == 3:
 
            ### 初回のみ
            if e_flag == 0:
                pygame.draw.circle(surface, (255,  0,  0), (now_x,now_y), M_SIZE, 0)
                pygame.draw.circle(surface, (224,224,224), (bak_x,bak_y), M_SIZE, 0)
                pygame.display.update()
                pygame.time.wait(100)
                e_flag = 1
 
            ### テキスト設定
            gol = Text("GOAL!",(224,224,255),(200,400))
            over = Text("GAMEOVER",(255,255,255),(200,400))
 
        ### 未ゴール
        if e_flag == 0:
 
            ### 移動キャラクター描画
            pygame.draw.circle(surface, (255,0,0), (now_x,now_y), M_SIZE, 0)
 
            ### 移動後通路の色に戻す
            if now_x != bak_x or now_y != bak_y:
                pygame.draw.circle(surface, (224,224,224), (bak_x,bak_y), M_SIZE, 0)
 
        ### 画面再描画
        pygame.display.update()
        pygame.time.wait(W_TIME)
 
        ### 位置保存
        bak_x = now_x
        bak_y = now_y
 
        ### イベント取得
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_LEFT:
                    if (now_x > 0      + B_SIZE) and (MAP[row][col-1] != 0):
                        col -= 1
                        now_x -= M_DOT
                if event.key == K_RIGHT:
                    if (now_x < WIDTH  - B_SIZE) and (MAP[row][col+1] != 0):
                        col += 1
                        now_x += M_DOT
                if event.key == K_UP:
                    if (now_y > 0      + B_SIZE) and (MAP[row-1][col] != 0):
                        row -= 1
                        now_y -= M_DOT
                if event.key == K_DOWN:
                    if (now_y < HEIGHT - B_SIZE) and (MAP[row+1][col] != 0):
                        row += 1
                        now_y += M_DOT       


def exit():
    pygame.quit()
    sys.exit()
 

if __name__ == "__main__":
    ### 画面初期化
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, F_SIZE)

    main()
    
import pygame as pg
import sys
from random import randint
import random


def check_bound(obj_rct, scr_rct):
    """
    obj_rct:こうかとんrct,または,爆弾rct
    scr_rct:スクリーンrct
    領域内：+1/領域外:-1
    """
    yoko1, tate1 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko1, yoko2 = -1, -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate1, tate2= -1, -1
    return yoko1, tate1

    yoko2, tate2 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko2 = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate2 = -1
    return yoko2, tate2


def main():
    pg.init()
    font1 = pg.font.Font(None, 300)
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("pg_bg.jpg") 
    bg_rct = bg_sfc.get_rect() #Surface 


    # 練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    # 爆弾の表示
    bomb1_sfc = pg.Surface((20,20)) # 空のSurface
    bomb2_sfc = pg.Surface((20,20)) # 空のSurface
    bomb1_sfc.set_colorkey((0, 0, 0)) #四隅の透過
    bomb2_sfc.set_colorkey((0, 0, 0)) #四隅の透過
    pg.draw.circle(bomb1_sfc,(255, 0, 0), (10, 10), 10)
    pg.draw.circle(bomb2_sfc,(0, 255, 0), (10, 10), 10)
    bomb1_rct = bomb1_sfc.get_rect()
    bomb2_rct = bomb2_sfc.get_rect()
    bomb1_rct.centerx = randint(0, scrn_rct.width)
    bomb1_rct.centery = randint(0, scrn_rct.height)
    bomb2_rct.centerx = randint(0, scrn_rct.width)
    bomb2_rct.centery = randint(0, scrn_rct.height)
    
    vx1, vy1 = +1, +1 # 練習6
    vx2, vy2 = +1, +1
    clock = pg.time.Clock()
    # 練習2
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        # 練習4
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP] : #縦座標-1
            tori_rct.centery -= 2
        if key_lst[pg.K_DOWN] : #縦座標+1
            tori_rct.centery += 2
        if key_lst[pg.K_LEFT] : #横座標-1
            tori_rct.centerx -= 2
        if key_lst[pg.K_RIGHT] : #横座標+1
            tori_rct.centerx += 2

        yoko1, tate1 = check_bound(tori_rct, scrn_rct)
        if yoko1 == -1:
            if key_lst[pg.K_LEFT]: #左キーを押したら
                tori_rct.centerx += 1
            if key_lst[pg.K_RIGHT]: #左キーを押したら
                tori_rct.centerx -= 1
        if tate1 == -1:
            if key_lst[pg.K_UP]: #上キーを押したら
                tori_rct.centery += 1
            if key_lst[pg.K_DOWN]: #下キーを押したら
                tori_rct.centery -= 1 
        
        yoko2, tate2 = check_bound(tori_rct, scrn_rct)
        if yoko2 == -1:
            if key_lst[pg.K_LEFT]: #左キーを押したら
                tori_rct.centerx += 1
            if key_lst[pg.K_RIGHT]: #左キーを押したら
                tori_rct.centerx -= 1
        if tate2 == -1:
            if key_lst[pg.K_UP]: #上キーを押したら
                tori_rct.centery += 1
            if key_lst[pg.K_DOWN]: #下キーを押したら
                tori_rct.centery -= 1 
        
        if key_lst[pg.K_a]: # Aキーを押したら
            vx1 = +2
            vx1 = +2
            vx2 = +2
            vy2 = +2

        if key_lst[pg.K_ESCAPE]: # Escキーを押したら
            return   

        if key_lst[pg.K_w]: # 大きさの変更
            bomb1_sfc = pg.Surface((30,30)) # 空のSurface
            bomb2_sfc = pg.Surface((30,30)) # 空のSurface
            pg.draw.circle(bomb1_sfc,(255, 0, 0), (15, 15), 15)
            pg.draw.circle(bomb2_sfc,(0, 255, 0), (15, 15), 15)
            bomb1_sfc.set_colorkey((0, 0, 0)) #四隅の透過
            bomb2_sfc.set_colorkey((0, 0, 0)) #四隅の透過
            

        scrn_sfc.blit(tori_sfc, tori_rct)
        yoko1, tate1 = check_bound(bomb1_rct, scrn_rct)
        yoko2, tate2 = check_bound(bomb2_rct, scrn_rct)
        vx1 *= yoko1
        vy1 *= tate1
        vx2 *= yoko2
        vy2 *= tate2
        bomb1_rct.move_ip(vx1, vy1) #練習6
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb1_sfc,bomb1_rct) #練習5
        scrn_sfc.blit(bomb2_sfc,bomb2_rct)
        
        # 練習8
        if tori_rct.colliderect(bomb1_rct) : # 赤色の爆弾に当たったら
            i = random.randint(0,9)
            tori_sfc = pg.image.load(f"fig/{i}.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)

        if tori_rct.colliderect(bomb2_rct) : # 青色の爆弾に当たったら
            text = font1.render("GAMEOVER", True, (0,0,0))
            scrn_sfc.blit(text, [200, 400])
            pg.display.update()
            clock.tick(0.5)
            return
            
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() #モジュールの初期化
    main()
    pg.quit() #モジュールの初期化を解除
    sys.exit() #プログラムを終了
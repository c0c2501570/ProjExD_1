import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)  # ← 追加（練習8：反転した背景画像）
    kk_img = pg.image.load("fig/3.png")               # ← 追加（練習3）
    kk_img = pg.transform.flip(kk_img, True, False)   # ← 追加（練習3）
    kk_rct = kk_img.get_rect()                        # ← 追加（練習10-1）
    kk_rct.center = 300, 200                          # ← 追加（練習10-2）
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()#練習１０－３全キ状態の取得
        dx, dy = -1, 0                  # ← 何もしなければ左に-1流れる（演習1-1）
        if key_lst[pg.K_UP]:
            dy -= 1
        if key_lst[pg.K_DOWN]:
            dy += 1
        if key_lst[pg.K_LEFT]:
            dx -= 1
        if key_lst[pg.K_RIGHT]:
            dx += 2                     # ← 右キーで+2（合計+1で右に進む：演習1-2）
        kk_rct.move_ip((dx, dy))        # ← 移動を1回にまとめる（演習2も同時に達成！）

        x = tmr % 3200# ← 追加（練習5）# 練習9：0〜3199で繰り返す
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])# ← [0, 0] を [-x, 0] に変更（練習5）# 2枚目（反転：練習7, 8）
        screen.blit(bg_img, [-x + 3200, 0])     # 3枚目（通常：練習9）
        screen.blit(kk_img, kk_rct)               # ← 追加（練習4）# ← [300, 200] を kk_rct に変更（練習10-5）
        pg.display.update()

        tmr += 1        
        clock.tick(200)# ← 10 を 200 に変更（練習6）


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
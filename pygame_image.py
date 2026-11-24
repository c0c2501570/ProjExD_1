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
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200# ← 追加（練習5）# 練習9：0〜3199で繰り返す
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])# ← [0, 0] を [-x, 0] に変更（練習5）# 2枚目（反転：練習7, 8）
        screen.blit(bg_img, [-x + 3200, 0])     # 3枚目（通常：練習9）
        screen.blit(kk_img, [300, 200])               # ← 追加（練習4）
        pg.display.update()

        tmr += 1        
        clock.tick(200)# ← 10 を 200 に変更（練習6）


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
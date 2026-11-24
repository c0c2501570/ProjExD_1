import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")               # ← 追加（練習3）
    kk_img = pg.transform.flip(kk_img, True, False)   # ← 追加（練習3）
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr# ← 追加（練習5）
        screen.blit(bg_img, [-x, 0])# ← [0, 0] を [-x, 0] に変更（練習5）
        screen.blit(kk_img, [300, 200])               # ← 追加（練習4）
        pg.display.update()
        tmr += 1        
        clock.tick(200)# ← 10 を 200 に変更（練習6）


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bbg_img = pg.transform.flip(bg_img,True,False)
    bg_img_2 = pg.image.load("ex01/fig/3.png")
    bg_img_2 = pg.transform.flip(bg_img_2,True,False)
    kk_img_2 = pg.transform.rotozoom(bg_img_2,1,1.0)
    kk_img_3 = pg.transform.rotozoom(bg_img_2,3,1.0)
    kk_img_4 = pg.transform.rotozoom(bg_img_2,5,1.0)
    kk_img_5 = pg.transform.rotozoom(bg_img_2,8,1.0)
    kk_img = pg.transform.rotozoom(bg_img_2,10,1.0)
    lis = [bg_img_2,kk_img_2,kk_img_3,kk_img_4,kk_img_5,kk_img,kk_img_5,kk_img_4,kk_img_3,kk_img_2]

    tmr = 0
    tmr2 = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x1 = tmr2%3200
        screen.blit(bg_img, [-x1, 0])
        screen.blit(bbg_img, [1600-x1, 0])
        screen.blit(bg_img, [3200-x1, 0])
        screen.blit(bg_img, [4800-x1, 0])
        screen.blit(lis[tmr%10], [300, 200])
        pg.display.update()
        tmr += 1
        tmr2 += 10
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
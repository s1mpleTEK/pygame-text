import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

pg.init()
pg.display.set_caption("pygame-text")
screen= pg.display.set_mode((800, 600))
clock = pg.time.Clock()
base_font = pg.font.Font(None, 32)
usr_txt = ''

input_rect = pg.Rect(200,200,140,32)
color1 = pg.Color('lightskyblue3')
color2 = pg.Color('red')

color = color2
active = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pg.KEYDOWN:
            if active == True:
                if event.key == pg.K_BACKSPACE:
                    usr_txt = usr_txt[:-1]
                else:
                    usr_txt += event.unicode

    screen.fill((0,0,0))

    if active:
        color = color1
    else:
        color = color2

    pg.draw.rect(screen, color, input_rect, 2)

    text_surface = base_font.render(usr_txt, True, (255,255,255))
    screen.blit(text_surface, (input_rect.x + 5 , input_rect.y + 5))

    input_rect.w = max(100, text_surface.get_width() + 10)

    pg.display.flip()
    clock.tick(60)
pg.quit()
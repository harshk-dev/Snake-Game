import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

FPS=60
FPSCLOCK=pg.time.Clock()
screen_width=1550
screen_height=810
screen=pg.display.set_mode((screen_width,screen_height),pg.RESIZABLE|pg.DOUBLEBUF)
game_sprites={}
with open("bin/high_score.txt") as f:
    high_score=f.read()

def welcome_screen():

    font1=pg.font.SysFont("arial",200)
    font2=pg.font.SysFont("arial",100)
    font3=pg.font.SysFont("arial",60)
    border_rect=pg.Rect(170,450,310,70)
    border_button_colour=(200,180,80)
    border_button_colour_change=False
    no_border_rect=pg.Rect(170,530,310,70)
    no_border_button_colour=(200,180,80)
    no_border_button_colour_change=False
    play_rect=pg.Rect(630,650,275,95)
    play_button_colour=(255,225,0)
    play_button_colour_change=False
    mx=0
    my=0
    mode_slection=""

    while True:
        for event in pg.event.get():
            if event.type==MOUSEMOTION:
                mx,my=event.pos
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pg.quit()
                exit()
            elif event.type==KEYDOWN and event.key==K_SPACE:
                return
            elif event.type==MOUSEBUTTONDOWN and event.button==1:
                if border_rect.collidepoint(event.pos):
                    mode_slection="bordered"
                    with open("bin/mode.txt","w") as f:
                        f.write("bordered")
                elif no_border_rect.collidepoint(event.pos):
                    mode_slection="no_border"
                    with open("bin/mode.txt","w") as f:
                        f.write("no_border")
                elif play_rect.collidepoint(event.pos):
                    return
            elif event.type==MOUSEMOTION and border_rect.collidepoint(event.pos):
                border_button_colour_change=True
            elif event.type==MOUSEMOTION and no_border_rect.collidepoint(event.pos):
                no_border_button_colour_change=True
            elif event.type==MOUSEMOTION and play_rect.collidepoint(event.pos):
                play_button_colour_change=True
        
        if border_button_colour_change:
            border_button_colour=(255,50,50)
        elif no_border_button_colour_change:
            no_border_button_colour=(50,255,50)
        elif play_button_colour_change:
            play_button_colour=(225,155,0)
        if not(border_rect.collidepoint(mx,my)):
            border_button_colour=(200,180,80)
            border_button_colour_change=False
        if not(no_border_rect.collidepoint(mx,my)):
            no_border_button_colour=(200,180,80)
            no_border_button_colour_change=False
        if not(play_rect.collidepoint(mx,my)):
            play_button_colour=(255,225,0)
            play_button_colour_change=False

        screen.blit(game_sprites["background"],(0,0))
        screen.blit(game_sprites["play_area"],(54,250))
        screen.blit(font1.render("SNAKE GAME",True,(0,255,255)),(100,20))
        screen.blit(game_sprites["large_point"],(750,430))
        screen.blit(game_sprites["snake"],(700,450))
        screen.blit(game_sprites["snake"],(680,450))
        screen.blit(game_sprites["snake"],(660,450))
        screen.blit(game_sprites["snake"],(640,450))
        screen.blit(game_sprites["snake"],(620,450))
        screen.blit(game_sprites["snake"],(600,450))
        screen.blit(game_sprites["snake"],(600,430))
        screen.blit(game_sprites["snake"],(600,410))
        if mode_slection=="bordered":
            pg.draw.rect(screen,(0,175,175),(165,445,320,80))
        elif mode_slection=="no_border":
            pg.draw.rect(screen,(0,175,175),(165,525,320,80))
        pg.draw.rect(screen,border_button_colour,(170,450,310,70))
        pg.draw.rect(screen,(0,0,0),(170,450,310,70),5)
        screen.blit(font3.render("Bordered",True,(0,0,0)),(200,450))
        pg.draw.rect(screen,no_border_button_colour,(170,530,310,70))
        pg.draw.rect(screen,(0,0,0),(170,530,310,70),5)
        screen.blit(font3.render("No Border",True,(0,0,0)),(186,530))
        pg.draw.rect(screen,play_button_colour,(630,650,275,95))
        pg.draw.rect(screen,(0,0,0),(630,650,275,95),5)
        screen.blit(font2.render("PLAY",True,(0,0,0)),(645,645))
        screen.blit(font2.render("Mode :-",True,(10,10,10)),(150,300))
        screen.blit(font2.render("High Score",True,(255,255,0)),(970,500))
        screen.blit(font2.render(high_score,True,(255,255,0)),(1200,620))
        pg.display.flip()
        FPSCLOCK.tick(FPS)
def main_game():
    global no_pop_large
    global no_pop_small
    global top_move
    global left_move
    global right_move
    global bottom_move
    global point_onsc
    global score_count
    global score
    which_score="small_point"
    font=pg.font.SysFont("Arial",45)
    largepoint_timerbar=0
    timerbar_com=False
    check=""
    x=0
    y=0
    snake_sleep=101
    small_point_animate=1
    largepoint_timerbar_animate=1
    with open("bin/mode.txt") as f:
            mode=f.read()

    while True:

        for event in pg.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pg.quit()
                exit()
            elif event.type==KEYDOWN and (event.key==K_w or event.key==K_UP or event.key==K_8) and bottom_move==False:
                top_move=True
                left_move=False
                right_move=False
                bottom_move=False
            elif event.type==KEYDOWN and (event.key==K_a or event.key==K_LEFT or event.key==K_4) and right_move==False:
                left_move=True
                top_move=False
                right_move=False
                bottom_move=False
            elif event.type==KEYDOWN and (event.key==K_d or event.key==K_RIGHT or event.key==K_6) and left_move==False:
                right_move=True
                top_move=False
                left_move=False
                bottom_move=False
            elif event.type==KEYDOWN and (event.key==K_s or event.key==K_DOWN or event.key==K_2) and top_move==False:
                bottom_move=True
                top_move=False
                left_move=False
                right_move=False
        
        if snake_sleep>100:
            check,x,y=border_collision()
            if check:
                if mode == "bordered":
                    return
                elif mode == "no_border":
                    no_border_mode(x,y)
            else:
                snake_movement()

            if point_onsc==False or timerbar_com:
                point_onsc=True
                score_cor=(randint(57,1472),randint(120,754))
                if score_count==5:
                    which_score="large_point"
                    score_count=0
                else :
                    which_score="small_point"
                    score_count+=1
                if timerbar_com:
                    timerbar_com=False

            if score_checker(score_cor,which_score):
                if which_score=="large_point":
                    no_pop_large=True
                    score+=10
                    if largepoint_timerbar>0:
                        largepoint_timerbar=0
                elif which_score=="small_point":
                    no_pop_small=True
                    score+=2
                point_onsc=False
            snake_sleep=0
            
        screen.blit(game_sprites["background"],(0,0))
        screen.blit(font.render(f"Score - {score}",True,(255,255,255)),(50,35))
        screen.blit(game_sprites["play_area"],(54,120))
        if which_score=="small_point":
            p,q=score_cor
            if int(small_point_animate)==1:
                screen.blit(game_sprites[which_score][0],(p,q))
            elif int(small_point_animate)==2:
                screen.blit(game_sprites[which_score][1],(p-1,q-1))
            elif int(small_point_animate)==3:
                screen.blit(game_sprites[which_score][2],(p-2,q-2))
            elif int(small_point_animate)==4:
                screen.blit(game_sprites[which_score][3],(p-1,q-1))
            small_point_animate+=0.1
            if small_point_animate>4:
                small_point_animate=1
        
        elif which_score=="large_point":
            screen.blit(game_sprites["large_point"],score_cor)
            if int(largepoint_timerbar_animate)==1:
                pg.draw.rect(screen,(255,0,0),(350,40,1007,50),2)
                if largepoint_timerbar<=988:
                    pg.draw.rect(screen,(255,0,0),(356,46,largepoint_timerbar,38))
                    largepoint_timerbar+=2
                    if largepoint_timerbar>=988:
                        timerbar_com=True
                        largepoint_timerbar=0
            elif int(largepoint_timerbar_animate)==2:
                pg.draw.rect(screen,(255,0,0),(348,39,1011,52),2)
                if largepoint_timerbar<=988:
                    pg.draw.rect(screen,(255,0,0),(354,45,largepoint_timerbar+4,38+2))
                    largepoint_timerbar+=2
                    if largepoint_timerbar>=988:
                        timerbar_com=True
                        largepoint_timerbar=0
            elif int(largepoint_timerbar_animate)==3:
                pg.draw.rect(screen,(255,0,0),(346,38,1015,54),2)
                if largepoint_timerbar<=988:
                    pg.draw.rect(screen,(255,0,0),(352,44,largepoint_timerbar+8,38+4))
                    largepoint_timerbar+=2
                    if largepoint_timerbar>=988:
                        timerbar_com=True
                        largepoint_timerbar=0
            elif int(largepoint_timerbar_animate)==4:
                pg.draw.rect(screen,(255,0,0),(344,37,1019,56),2)
                if largepoint_timerbar<=988:
                    pg.draw.rect(screen,(255,0,0),(350,43,largepoint_timerbar+12,38+6))
                    largepoint_timerbar+=2
                    if largepoint_timerbar>=988:
                        timerbar_com=True
                        largepoint_timerbar=0
            elif int(largepoint_timerbar_animate)==5:
                pg.draw.rect(screen,(255,0,0),(342,36,1023,58),2)
                if largepoint_timerbar<=988:
                    pg.draw.rect(screen,(255,0,0),(348,42,largepoint_timerbar+16,38+8))
                    largepoint_timerbar+=2
                    if largepoint_timerbar>=988:
                        timerbar_com=True
                        largepoint_timerbar=0
            elif int(largepoint_timerbar_animate)==6:
                pg.draw.rect(screen,(255,0,0),(344,37,1019,56),2)
                if largepoint_timerbar<=988:
                    pg.draw.rect(screen,(255,0,0),(350,43,largepoint_timerbar+12,38+6))
                    largepoint_timerbar+=2
                    if largepoint_timerbar>=988:
                        timerbar_com=True
                        largepoint_timerbar=0
            elif int(largepoint_timerbar_animate)==7:
                pg.draw.rect(screen,(255,0,0),(346,38,1015,54),2)
                if largepoint_timerbar<=988:
                    pg.draw.rect(screen,(255,0,0),(352,44,largepoint_timerbar+8,38+4))
                    largepoint_timerbar+=2
                    if largepoint_timerbar>=988:
                        timerbar_com=True
                        largepoint_timerbar=0
            elif int(largepoint_timerbar_animate)==8:
                    pg.draw.rect(screen,(255,0,0),(348,39,1011,52),2)
                    if largepoint_timerbar<=988:
                        pg.draw.rect(screen,(255,0,0),(354,45,largepoint_timerbar+4,38+2))
                        largepoint_timerbar+=2
                        if largepoint_timerbar>=988:
                            timerbar_com=True
                            largepoint_timerbar=0
            largepoint_timerbar_animate+=0.1
            if largepoint_timerbar_animate>8:
                largepoint_timerbar_animate=1

        for coor in snake_coordinate:
            screen.blit(game_sprites["snake"],coor)
        pg.display.flip()
        FPSCLOCK.tick(FPS)
        
        if collision():
            return
        snake_sleep+=10

def collision():
    x,y=snake_coordinate[0]
    for p,q in snake_coordinate:
        if y==q and x==p:
            pass
        else:
            if left_move:
                if x==p+20 and y==q:
                    return True
            if right_move:
                if x+20==p and y==q:
                    return True
            if top_move:
                if x==p and y==q+20:
                    return True
            if bottom_move:
                if x==p and y+20==q:
                    return True
    
def border_collision():
    x,y=snake_coordinate[0]
    if x+20>=1440+54 or x<=54 or y<=120 or y+20>=656+120:
        return (True,x,y)
    else:
        return (False,0,0)
    
def score_checker(score_cor,which_score):
    x,y=score_cor
    if which_score=="small_point":
        if snake_coordinate[0][0]+10>x-10 and snake_coordinate[0][0]+10<x+35:
            if snake_coordinate[0][1]+10>y-10 and snake_coordinate[0][1]+10<y+35 :
                return True
    elif which_score=="large_point":
        if snake_coordinate[0][0]+10>x-10 and snake_coordinate[0][0]+10<x+35:
            if snake_coordinate[0][1]+10>y-10 and snake_coordinate[0][1]+10<y+35 :
                return True

def no_border_mode(x,y):
    global no_pop_small
    global no_pop_large
    global i
    
    if top_move:
        y=game_sprites["play_area"].get_height()+100
    elif left_move:
        x=game_sprites["play_area"].get_width()+34
    elif right_move:
        x=55
    elif bottom_move:
        y=121

    snake_coordinate.insert(0,(x,y))

    if no_pop_small==False and no_pop_large==False:
        snake_coordinate.pop(len(snake_coordinate)-1)
    elif no_pop_small==True:
        if i==2:
            i=0
            no_pop_small=False
        else:
            i+=1
    elif no_pop_large==True:
        if i==10:
            i=0
            no_pop_large=False
        else:
            i+=1
    
def snake_movement():
    global snake_coordinate
    global no_pop_small
    global no_pop_large
    global i
    x,y=snake_coordinate[0]
    x_coor=x
    y_coor=y
    if top_move:
        y_coor=y-20
    elif left_move:
        x_coor=x-20   
    elif right_move:
        x_coor=x+20   
    elif bottom_move:
        y_coor=y+20
    if no_pop_small==False and no_pop_large==False:
        snake_coordinate.pop(len(snake_coordinate)-1)
    elif no_pop_small==True:
        if i==2:
            i=0
            no_pop_small=False
        else:
            i+=1
    elif no_pop_large==True:
        if i==10:
            i=0
            no_pop_large=False
        else:
            i+=1
    
    snake_coordinate.insert(0,(x_coor,y_coor))

def snake_death():
    while True:
        for event in pg.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pg.quit()
                exit()
        for co in snake_coordinate:
            screen.blit(game_sprites["snake"],co)

        sleep(0.5)
        return

def hig_score():
    with open("bin/high_score.txt") as f :
        high_score=f.read()
    if score>int(high_score):
        with open("bin/high_score.txt","w") as f:
            f.write(str(score))

if __name__=="__main__":
    pg.init()
    pg.display.set_caption("Snake Game")

    game_sprites["background"]=pg.image.load("gallery/background.png").convert()
    game_sprites["play_area"]=pg.image.load("gallery/play_area.png").convert()
    game_sprites["snake"]=pg.image.load("gallery/snake.png").convert_alpha()
    game_sprites["small_point"]=(pg.image.load("gallery/small_point_1.png").convert_alpha(),
                                pg.image.load("gallery/small_point_2.png").convert_alpha(),
                                pg.image.load("gallery/small_point_3.png").convert_alpha(),
                                pg.image.load("gallery/small_point_4.png").convert_alpha())
    game_sprites["large_point"]=pg.image.load("gallery/large_point.png").convert_alpha()

    while True:
        
        snake_coordinate=[(500,500),(500,520)]
        i=0
        score=0
        score_count=0
        no_pop_small=False
        no_pop_large=False
        point_onsc=False
        top_move=False
        left_move=False
        right_move=True
        bottom_move=False

        welcome_screen()
        main_game()
        snake_death()
        hig_score()
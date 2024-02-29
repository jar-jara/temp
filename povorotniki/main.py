from pygame import *
import pygame as pg

pg.init()

W, H = 600, 500
screen = pg.display.set_mode((W, H))

pg.display.set_caption("GAME POVOROTNIKI")
clock = pg.time.Clock()

player_anim_count = 0
bg_x = 0

player_speed = 10
player_x = 150
player_y = 300

is_jump = False
jump_count = 8

walk_left = [
    pg.image.load('player_left/player_left1.png').convert_alpha(),
    pg.image.load('player_left/player_left2.png').convert_alpha(),
    pg.image.load('player_left/player_left3.png').convert_alpha(),
    pg.image.load('player_left/player_left4.png').convert_alpha()]

walk_right = [
    pg.image.load('player_right/player_right1.png').convert_alpha(),
    pg.image.load('player_right/player_right2.png').convert_alpha(),
    pg.image.load('player_right/player_right3.png').convert_alpha(),
    pg.image.load('player_right/player_right4.png').convert_alpha()]

car = pg.image.load('cars.jpg').convert_alpha()

game = True
while game:
    screen.fill(pg.Color('blue'))
    #screen.blit(car, (150, 150))

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    
    if keys[pg.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pg.K_RIGHT] and player_x < 350:
        player_x += player_speed
    if not is_jump:
        if keys[pg.K_SPACE]:
            is_jump = True

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()

    pg.display.update()

    clock.tick(25)
    


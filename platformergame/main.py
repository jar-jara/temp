from pygame import *
import pygame as pg


pg.init()

window = pg.display.set_mode((1280, 720))
pg.display.set_caption('Platformer Game Pygame')
icon = pg.image.load('icon.png').convert_alpha()
pg.display.set_icon(icon)
clock = pg.time.Clock()


bg = pg.image.load('maxresdefault.jpg').convert_alpha()
ghost = pg.image.load('ghost.png').convert_alpha()
#ghost_x = 1202
ghost_list_in_game = []

walk_left = [
    pg.image.load('player_left/player_left1.png').convert_alpha(),
    pg.image.load('player_left/player_left2.png').convert_alpha(),
    pg.image.load('player_left/player_left3.png').convert_alpha(),
    pg.image.load('player_left/player_left4.png').convert_alpha()
]

walk_right = [
    pg.image.load('player_right/player_right1.png').convert_alpha(),
    pg.image.load('player_right/player_right2.png').convert_alpha(),
    pg.image.load('player_right/player_right3.png').convert_alpha(),
    pg.image.load('player_right/player_right4.png').convert_alpha()
]

player_anim_count = 0
bg_x = 0

player_speed = 10
player_x = 150
player_y = 540

is_jump = False
jump_count = 8


bg_sound = pg.mixer.music.load('sounds/bgsounds2.mp3')
pg.mixer.music.play()

ghost_timer = pg.USEREVENT + 1
pg.time.set_timer(ghost_timer, 2500)

run = True
while  run:
    
    window.blit(bg, (bg_x, 0))
    window.blit(bg, (bg_x + 1200, 0))
    #window.blit(ghost, (ghost_x, 550))

    player_rect = walk_left[0].get_rect(topleft = (player_x, player_y))
    #ghost_rect = ghost.get_rect(topleft=(ghost_x, 550))
    if ghost_list_in_game:
        for el in ghost_list_in_game:
            window.blit(ghost, el)
            el.x -= 10

            if player_rect.colliderect(el):
                print("YOU LOSE")

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        window.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        window.blit(walk_right[player_anim_count], (player_x, player_y))

    
    if keys[pg.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pg.K_RIGHT] and player_x < 350:
        player_x += player_speed
    
    if not is_jump:
        if keys[pg.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8

        
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1


    bg_x -= 2
    if bg_x == -1200:
        bg_x = 0

    #ghost_x -= 10

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft = (1202, 550)))


    clock.tick(15)


from pygame import *
import pygame as pg
from time import *
#import kartegame

pg.init()
font = pg.font.Font(None, 36)

W, H = 1080, 720
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
pg.display.set_caption("BuSines GAME")

credits = 0
reputation = 0
man = 0
credits = 
limit = 0
  

def draw_text(screen, text, x, y):
    text_surface = font.render(text, False, (0, 0, 0))
    screen.blit(text_surface, (x, y))

def plan_game():
    draw_text(screen, f"Начало игры!\nНажми на a, чтобы прибавить 100 рублей\nНажми d, чтобы убавить 100 рублей\nГлавное помни - НЕ НАЖИМАЙ НА O, ИНАЧЕ....", 10, 40)

class Karta():
    def __init__(self, credits, man, reputation):
        self.credits = credits
        self.man = man
        self.reputation = reputation
    def print_info(self):
        print('Денег:',self.credits)
        print('рабочих:',self.man)
        print('репутации:',self.reputation)


class ImageButton:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pg.image.load(hover_image_path)
            self.hover_image = pg.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pg.mixer.Sound(sound_path)
        self.is_hovered = False
    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pg.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    #def cheeeeeeee

    



#kards = [
karta1 = Karta(5000, 2, 10),
karta_two = Karta('1000', '5', '20'),
karta_three = Karta('10000', '10', '-50')




def draw_text(screen, text, x, y):
    surface_text = font.render(text, False, (0, 0, 0))
    screen.blit(surface_text, (x, y))


def right_text(screen, text, x, y):
    text_right = font.render(text, False, (0, 0, 0))
    screen.blit(text_right, (x, y))


def reputation_text(screen, text, x, y):
    text_right = font.render(text, False, (0, 0, 0))
    screen.blit(text_right, (x, y))


def many_man(screen, text, x, y):
    many_text = font.render(text, False, (pg.Color('red')))
    screen.blit(many_text, (x, y))


    







finish = False
game = True
while game:

    
    #screen.blit(text_surface, (0, 0))


    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                credits += 100 
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                credits -= 100
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                credits += 100
                reputation +=10
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                credits -= 100
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                credits += 1000
                reputation +=10
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_o:
                credits -= 10000
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                man += 1
                reputation +=10
                credits -= 100
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_2:
                man -= 1
        if event.type == pg. KEYDOWN:
            if event.key == pg.K_3:
                screen.fill(pg.Color('green')) 
                
        
    if not finish:
        screen.fill(pg.Color("white"))
        reputation_text(screen, f"Добро пожаловать!", 350, 500)
        
        
        if credits <= -10000 or credits >= 10000:
            reputation_text(screen, f"THE END!", 500, 300)
            sleep(1)
            break



        if man >= 20:
            many_man(screen, f"Слишком много рабочих! => {man}", 500, 300)

        if man < limit:
            many_man(screen, f"Ты пытаешься удалить пустого человека!", 400, 300)
            man = 0

        draw_text(screen, f"Очки: {credits}", 10, 10)
        right_text(screen, f"Добавлено человек: {man}", 800, 0)
        reputation_text(screen, f"Репутация: {reputation}", 10, 40)
        
        
        
       
        draw_text(screen, f"Возмёшь карточку?: денег = 5000,%рабочих = 3,\nрепутации = 10", 10, 300)


    pg.display.flip()
    clock.tick(50)

pg.display.update()
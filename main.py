from random import randint
from pygame import *
from time import time as timer

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_widht, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_widht, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3

wall1 = Player('racket.png', 10, 200, 5, 20, 100)
wall2 = Player('racket.png', 670, 200, 5, 20, 100)
ball = GameSprite('tenis_ball.png', 100, 200, 3, 50, 50)

run = True
finish = False
FPS = 40
clock = time.Clock()

font.init()
font1 = font.SysFont('Arial', 30)
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))

while run:   
    for e in event.get():
       if e.type == QUIT:
           run = False
    if not finish: 
        window.blit(background, (0, 0))
        wall1.reset()
        wall1.update_l()
        wall2.reset()
        wall2.update_r()
        ball.reset()
        ball.update()
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))
    if sprite.collide_rect(ball, wall1) or sprite.collide_rect(ball, wall2):
        speed_x *= -1
    display.update()
    clock.tick(FPS)
    
    

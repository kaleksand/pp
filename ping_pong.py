from pygame import *
from random import randint

win_wight = 1000
win_hight = 600
FPS = 60
clock = time.Clock()
speed = 5


window = display.set_mode((win_wight, win_hight))
display.set_caption('ping_pong window')
background = transform.scale(image.load('inline_image_preview.jpg'), (win_wight, win_hight))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Playear(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hight - 80:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_hight - 80:
            self.rect.y += self.speed

player1 = Playear('b5cfe7f968df0ed5437b4eb5fbfbea3e.png', 100, 300, speed, 100,130) 
player2 = Playear('b5cfe7f968df0ed5437b4eb5fbfbea3e.png', 800, 300, speed, 100,130)
ball = GameSprite('Tennis-Ball-Transparent-Background.png', 500, 400,  speed, 100, 100) 
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0, 0))

    player1.update_l()
    player1.reset() 
    player2.update_r()
    player2.reset()
    ball.reset()
    clock.tick(FPS)
    display.update()   





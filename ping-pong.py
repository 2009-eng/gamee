from pygame import *
class win_width: 
    def update(self):
       keys = key.get_pressed()
       if keys[K_d] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_a] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_DOWN] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
          
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
class Ball(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
class win_height(GameSprite):
speed_x = 3
speed_y = 3
game = True
finish = False

while game:
    
    #...
    if finish != True:
         Ball.rect.x += speed_x
         Ball.rect.y += speed_y

    if Ball.rect.x > win_height-50 or Ball.rect.y < 0:
        speed_y *= -1

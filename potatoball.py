
import random
from potatoboss import Potato
import pygame
from pygame import image
import pygame




class Pball:
    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed



    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))

    def allballs(self):
        self.hitbox.x -= self.speed
        if self.hitbox.x <  0:
            self.hitbox.x = self.hitbox.x = 490
            self.hitbox.y = self.hitbox.y = 420

potatoballs = []

for i in range(5):
    potatoballs.append(Pball(490,420,  50, 50, "7b72a9f27ed5bad6a836b73860616338a25c2b34r1-220-220v2_hq.jpg", 4 ))








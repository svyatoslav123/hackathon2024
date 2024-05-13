
import random
from potatoboss import Potato
import pygame
from pygame import image
import pygame



potatoballs = []

class Pball:
    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.hp = 1
        self.i = i
        #то саме як в патроні




    def draw(self, window):

        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
        # то саме як в патроні

    def allballs(self):
        self.hitbox.x -= self.speed
        if self.hitbox.x <  0:
            self.hitbox.x = self.hitbox.x = 490
            self.hitbox.y = self.hitbox.y = 420
            # то саме як в патроні
for i in range(5):
    potatoballs.append(Pball(490, 420, 60, 60, "52-removebg-preview.png", 4))









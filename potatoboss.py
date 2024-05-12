import pygame

class Potato:
    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.hitbox.w = w
        self.hitbox.h = h
        self.counter = 0

    def draw(self, window):

        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
    def allboss(self):
        self.animation('stayb')
    def animation(self,kind):
        if kind == 'stayb':
            self.counter += 1
            if 0 <= self.counter < 20:
                self.photo = pygame.transform.scale(pygame.image.load('32-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))
            elif 20 <= self.counter < 40:
                self.photo = pygame.transform.scale(pygame.image.load('33-removebg-preview (3).png'), (self.hitbox.w, self.hitbox.h))
            if self.counter > 40:
               self.counter = 0




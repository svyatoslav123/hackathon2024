import pygame
from bullet import Bullet
class Player:
    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.hitbox.w = w
        self.hitbox.h = h
        self.isJumping = self.jump
        self.jumpCount = 15
        self.bullets = []
        self.counter = 0

    def draw(self, window):

        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
        for bullet in self.bullets:
            bullet.draw(window)
            bullet.move()


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
        elif keys[pygame.K_d]:
            self.hitbox.x += self.speed
            self.animation('go_left')
        elif keys[pygame.K_a]:
            self.hitbox.x -= self.speed
            self.animation('go_right')
        elif keys[pygame.K_e]:
            print(1)
            self.bullets.append(Bullet(self.hitbox.x+60, self.hitbox.y+31,35,17,"Peashooter.webp",1))
            self.animation('shoot')
        else:
            self.animation('stay')

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.isJumping = True

        if self.isJumping:
            self.hitbox.y -= self.jumpCount
            self.jumpCount -= 1
            if self.jumpCount == -16:
                self.isJumping = False
                self.jumpCount = 15
    def animation(self,kind):
        if kind == 'stay':
            self.counter += 1
            if 0 <= self.counter < 20:
                self.photo = pygame.transform.scale(pygame.image.load('photo_2024-05-12_17-11-11-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))
            elif 20 <= self.counter < 40:
                self.photo = pygame.transform.scale(pygame.image.load('photo_2024-05-12_17-11-07-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))
            elif 40 <= self.counter < 60:
                self.photo = pygame.transform.scale(pygame.image.load('photo_2024-05-12_17-10-59-removebg-preview (1).png'), (self.hitbox.w, self.hitbox.h))


            if self.counter > 60:
                self.counter = 0
        elif kind == 'go_left':
            self.counter += 1
            if 0 <= self.counter < 10:
                self.photo = pygame.transform.scale(pygame.image.load('1-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))
            elif 10 <= self.counter < 20:
                self.photo = pygame.transform.scale(pygame.image.load('2-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))
            elif 20 <= self.counter < 30:
                self.photo = pygame.transform.scale(pygame.image.load('3-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))
            elif 30 <= self.counter < 40:
                self.photo = pygame.transform.scale(pygame.image.load('4-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))
            elif 40 <= self.counter < 50:
                self.photo = pygame.transform.scale(pygame.image.load('5-removebg-preview.png'), (self.hitbox.w, self.hitbox.h))


            if self.counter > 50:
                self.counter = 0

        elif kind == 'go_right':
            self.counter += 1
            if 0 <= self.counter < 10:
                self.photo = pygame.transform.scale(pygame.image.load('6-removebg-preview.png'),(self.hitbox.w, self.hitbox.h))
            elif 10 <= self.counter < 20:
                self.photo = pygame.transform.scale(pygame.image.load('7-removebg-preview.png'),(self.hitbox.w, self.hitbox.h))
            elif 20 <= self.counter < 30:
                self.photo = pygame.transform.scale(pygame.image.load('8-removebg-preview.png'),(self.hitbox.w, self.hitbox.h))
            elif 30 <= self.counter < 40:
                self.photo = pygame.transform.scale(pygame.image.load('9-removebg-preview.png'),(self.hitbox.w, self.hitbox.h))
            elif 40 <= self.counter < 50:
                self.photo = pygame.transform.scale(pygame.image.load('10-removebg-preview.png'),(self.hitbox.w, self.hitbox.h))


            if self.counter > 50:
                self.counter = 0

        elif kind == 'shoot':
            self.counter += 1
            if 0 <= self.counter < 20:
                self.photo = pygame.transform.scale(pygame.image.load('11-removebg-preview.png'),(self.hitbox.w, self.hitbox.h))
            elif 20 <= self.counter < 35:
                self.photo = pygame.transform.scale(pygame.image.load('12-removebg-preview.png'),(self.hitbox.w, self.hitbox.h))


            if self.counter > 35:
                self.counter = 0






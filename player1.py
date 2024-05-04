import pygame

class Player:
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


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
        elif keys[pygame.K_s]:
            self.hitbox.y += self.speed
        elif keys[pygame.K_d]:
            self.hitbox.x += self.speed
        elif keys[pygame.K_a]:
            self.hitbox.x -= self.speed



    def animation(self):

            self.counter += 1
            if 0 <= self.counter < 15:
                self.photo = pygame.transform.scale(pygame.image.load('Знімок екрана 2024-05-03 224612.jpg'), (self.hitbox.w, self.hitbox.h))
            elif 15 <= self.counter < 30:
                self.photo = pygame.transform.scale(pygame.image.load('Знімок екрана 2024-05-03 224550.jpg'), (self.hitbox.w, self.hitbox.h))
            elif 30 <= self.counter < 45:
                self.photo = pygame.transform.scale(pygame.image.load('Знімок екрана 2024-05-03 224533.jpg'), (self.hitbox.w, self.hitbox.h))


            if self.counter > 45:
                self.counter = 0
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



class Cuphead(Player):
    def __init__(self, x, y, w, h, img, speed):
        Player.__init__(self, x, y, w, h, img, speed)
        self.counter = 0

    def animation(self):

            self.counter += 1
            if 0 <= self.counter < 20:
                self.image = pygame.transform.scale(pygame.image.load('Знімок екрана 2024-05-03 224612.jpg'), (self.hitbox.w, self.hitbox.h))
            elif 20 <= self.counter < 40:
                self.image = pygame.transform.scale(pygame.image.load('Знімок екрана 2024-05-03 224550.jpg'), (self.hitbox.w, self.hitbox.h))
            elif 40 <= self.counter < 60:
                self.image = pygame.transform.scale(pygame.image.load('Знімок екрана 2024-05-03 224533.jpg'), (self.hitbox.w, self.hitbox.h))


            if self.counter > 60:
                self.counter = 0
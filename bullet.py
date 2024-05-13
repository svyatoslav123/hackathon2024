import pygame
bullets = []
class Bullet:


    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        #створювання класу патрона

    def draw(self, window):

        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
        #відмальовування патрона

    def move(self):
        self.hitbox.x += self.speed
        #створення руху патрона
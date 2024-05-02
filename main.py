import pygame
from player1 import Player

pygame.init()

window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
pygame.mixer.init()

sound = pygame.mixer.music.load("07 Botanic Panic.mp3")
pygame.mixer.music.play(-5)




background = pygame.transform.scale(
    pygame.image.load("HD-wallpaper-video-game-cuphead.jpg"), (800, 500)
)
cuphead = Player(20, 420, 80, 80, "CupheadCharacter (1).webp", 5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()




    window.blit(background, (0, 0))
    cuphead.move()
    cuphead.draw(window)
    pygame.display.flip()
    fps.tick(60)
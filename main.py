import pygame




window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()

background = pygame.transform.scale(
    pygame.image.load("HD-wallpaper-video-game-cuphead.jpg"), (800, 500)
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()




    window.blit(background, (0, 0))

    pygame.display.flip()
    fps.tick(60)
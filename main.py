from pygame import*
import sys
from player1 import Player

from potatoboss import Potato
from potatoball import *
pygame.init()

window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
pygame.mixer.init()






background = pygame.transform.scale(
    pygame.image.load("HD-wallpaper-video-game-cuphead.jpg"), (800, 500)
)
cuphead = Player(20, 420, 80, 100, "CupheadCharacter (1).webp", 5)
potato = Potato(450, 200, 300, 300, "Moetato (1).webp")
menu_bg = Player(0, 0, 800, 500, 'e62e977d9822beb408f0ec28b6dc8a313c94d3e5r1-800-480v2_uhq.jpg', 0)
btn_play = Player(250, 370, 250, 100, 'Play-Button.jpg', 0)

btn_menu = Player(100, 100, 50, 50, '54447.png', 0)

screen = 'menu'
game = True
while game:
    if screen == 'menu':
        menu_bg.draw(window)
        btn_play.draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_play.hitbox.collidepoint(x, y):
                    screen = 'game'
                    sound = pygame.mixer.music.load("07 Botanic Panic.mp3")
                    pygame.mixer.music.play(-5)

        display.update()
        fps.tick(60)

    if screen == 'game':
        window.fill((255, 200, 200))
        cuphead.draw(window)
        btn_menu.draw(window)


        #for pball in potatoballs:
            #pball.draw(window)
            #pball.move()
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_play.hitbox.collidepoint(x, y):
                    screen = 'menu'


            window.blit(background, (0, 0))
            potato.draw(window)


            cuphead.move()
            cuphead.animation()
            cuphead.draw(window)
            for pball in potatoballs:
                pball.draw(window)
            pygame.display.flip()
            fps.tick(60)
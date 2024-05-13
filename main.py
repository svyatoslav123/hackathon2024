from pygame import *
import sys
from player1 import Player
from bullet import *
from potatoboss import Potato
from potatoball import *
pygame.init()
#підключення всіх неопхідних елементів для гри
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
pygame.mixer.init()
#створювання вікна





background = pygame.transform.scale(
    pygame.image.load("HD-wallpaper-video-game-cuphead.jpg"), (800, 500)
)
#створювання самого фону для гри
cuphead = Player(20, 420, 80, 100, "CupheadCharacter (1).webp", 5)
potato = Potato(450, 200, 300, 300, "Moetato (1).webp",0)
menu_bg = Player(0, 0, 800, 500, 'e62e977d9822beb408f0ec28b6dc8a313c94d3e5r1-800-480v2_uhq.jpg', 0)
btn_play = Player(250, 370, 250, 100, 'Play-Button.jpg', 0)
btn_menu = Player(0, 20, 250, 100, '54447.png', 0)
btn_retry = Player(250, 370, 250, 100, '87.jpg', 0)
knokout= Player(0, 0, 700, 500, 'fhxhe3rvqaaprhc.webp', 0)
lose = Player(150, 0, 400, 500, 'завантаження (1).jpg', 0)
#створювання кнопок спрайті в і тд

screen = 'menu'
game = True
while game:
    #створювання циклу
    if screen == 'menu':
        menu_bg.draw(window)
        btn_play.draw(window)
        #створювання меню

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_play.hitbox.collidepoint(x, y):
                    #підключення кнопки
                    screen = 'game'
                    sound = pygame.mixer.music.load("07 Botanic Panic.mp3")
                    pygame.mixer.music.play(-5)
                    #встановлення музики

        display.update()
        fps.tick(60)

    if screen == 'game':
        window.fill((255, 200, 200))
        cuphead.draw(window)
        btn_menu.draw(window)
        # створювання екрану гра

        for bullet in cuphead.bullets:
            if potato.hitbox.colliderect(bullet.hitbox):
               potato.hp -= 2
               cuphead.bullets.remove(bullet)
               if potato.hp < 1:
                  screen = "win"
        for bullet in cuphead.bullets:
            if pball.hitbox.colliderect(bullet.hitbox):
               cuphead.bullets.remove(bullet)
        for pball in potatoballs:
            if cuphead.hitbox.colliderect(pball.hitbox):
                cuphead.hp -= 1

                if cuphead.hp < 1:

                   screen = "lose"
                   # умови налаштування для гри

        for event in pygame.event.get():
            if event.type == QUIT:
                game = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_play.hitbox.collidepoint(x, y):
                    screen = 'menu'


        window.blit(background, (0, 0))
        potato.draw(window)
        potato.allboss()

        for pball in potatoballs:
            pball.draw(window)
            pball.allballs()
        cuphead.move()
        cuphead.jump()
        cuphead.draw(window)

        pygame.display.flip()
        fps.tick(60)
    if screen == "win":
        window.fill((0, 255, 0))
        knokout.draw(window)
        sound = pygame.mixer.music.load("Voicy_ Knockout SFX.mp3")
        pygame.mixer.music.play(-1)
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False


        pygame.display.flip()
        fps.tick(60)
    if screen == "lose":
        window.fill((255, 0, 0))
        lose.draw(window)
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if btn_retry.hitbox.collidepoint(x, y):
                screen = 'game'






        pygame.display.flip()
        fps.tick(60)



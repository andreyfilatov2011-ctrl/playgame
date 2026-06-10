import pygame

from condfig import HEIGHT, WIDTH
from player import Player
pygame.init()

background = pygame.image.load("imj/bag.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
back_rect = background.get_rect()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    player = Player()


    while True:
        # 1 Cчитывание
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit("GAME OVER")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()



        # 2 Обновление

        player.update()


        # 3 Отрисовка
        screen.fill("lightblue")
        screen.blit(background, back_rect)

        player.draw(screen=screen)




        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()

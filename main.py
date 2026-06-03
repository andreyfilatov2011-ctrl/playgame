import pygame

from condfig import HEIGHT, WIDTH
from player import Player
pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    # Todo создать object
    player = Player()

    player.update()
    player.draw()
    while True:
        # 1 Cчитывание
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit("GAME OVER")
        # 2 Обновление
        #updste
        def player():


        # 3 Отрисовка
        screen.fill("lightblue")
        #draw

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()

import pygame

from condfig import HEIGHT, WIDTH

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    # Todo создать object

    while True:
        # 1 Cчитывание
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit("GAME OVER")
        # 2 Обновление
        #updste

        # 3 Отрисовка
        screen.fill("lightblue")
        #draw

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()

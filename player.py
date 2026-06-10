import pygame
from condfig import SPEED, WIDTH, HEIGHT

GRAVITY = 0.8  # лучше 0.8, чем 1 (более плавно)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imj/stay.png")
        self.image =
        self.rect = self.image.get_rect(midbottom=(100, 500))
        self.speed_x = 0
        self.velocity = 0

    def update(self):
        # Гравитация
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        # Горизонтальное движение
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += SPEED

        # Границы по горизонтали
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH

        # Граница по земле (остановка падения)
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0  # на земле скорость обнуляем

        if self.rect.bottom >= WIDTH:
            self.rect.bottom = WIDTH

    def jump(self):
        # Прыжок только с земли
        if self.rect.bottom >= HEIGHT:
            self.velocity = -18  # отрицательная скорость = прыжок вверх

    def draw(self, screen):
        screen.blit(self.image, self.rect)


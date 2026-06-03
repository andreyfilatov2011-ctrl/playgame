import pygame

from condfig import SPEED, WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill("blue")
        self.rect = self.image.get_rect(midbottom=(100, 500))
        self.speed_x = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += SPEED

        if self.rect.left > WIDTH:
            self.rect.right = 0

        if self.rect.left < 0:
            self.rect.left = 800


    def draw(self, screen):
        screen.blit(self.image, self.rect)

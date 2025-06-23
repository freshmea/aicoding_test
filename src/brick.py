# 코파일럿에 의해 만들어짐.

import pygame


class Brick(pygame.sprite.Sprite):
    """키보드로 움직일 수 있는 벽돌 스프라이트 클래스."""
    def __init__(self, x, y, width=60, height=20, color=(0, 128, 255)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

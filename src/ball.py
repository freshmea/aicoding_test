# 코파일럿에 의해 만들어짐.

import pygame


class Ball(pygame.sprite.Sprite):
    """벽돌과 탄성 충돌하는 공 스프라이트 클래스."""
    def __init__(self, x: int, y: int, radius: int = 10, color=(255, 0, 0), speed_x: int = 4, speed_y: int = 4):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, brick_group: pygame.sprite.Group, screen_rect: pygame.Rect):
        # 이동
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 화면 경계 충돌
        if self.rect.left <= screen_rect.left or self.rect.right >= screen_rect.right:
            self.speed_x *= -1
        if self.rect.top <= screen_rect.top or self.rect.bottom >= screen_rect.bottom:
            self.speed_y *= -1

        # 벽돌과 충돌 체크 및 탄성 반사
        collided_brick = pygame.sprite.spritecollideany(self, brick_group) # type: ignore
        if collided_brick:
            # 충돌 방향 판정
            if abs(self.rect.bottom - collided_brick.rect.top) < self.radius or \
               abs(self.rect.top - collided_brick.rect.bottom) < self.radius:
                self.speed_y *= -1
            else:
                self.speed_x *= -1

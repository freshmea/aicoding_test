# 코파일럿에 의해 만들어짐.

import sys
import unittest

import pygame

sys.path.append("./src")
from ball import Ball
from brick import Brick


class TestBrick(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.brick = Brick(x=100, y=100)

    def tearDown(self):
        pygame.quit()

    def test_brick_move_left(self):
        # 키 배열 크기를 pygame.key.get_scancode_from_key(pygame.K_LAST) + 1로 동적으로 결정
        key_array_size = max(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) + 1
        keys = [False] * key_array_size
        keys[pygame.K_LEFT] = True
        old_x = self.brick.rect.x
        self.brick.update(keys)
        self.assertLess(self.brick.rect.x, old_x)

    def test_brick_move_right(self):
        key_array_size = max(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) + 1
        keys = [False] * key_array_size
        keys[pygame.K_RIGHT] = True
        old_x = self.brick.rect.x
        self.brick.update(keys)
        self.assertGreater(self.brick.rect.x, old_x)

class TestBall(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.brick = Brick(x=100, y=100)
        self.ball = Ball(x=110, y=90)
        self.brick_group = pygame.sprite.Group(self.brick) # type: ignore
        self.screen_rect = pygame.Rect(0, 0, 200, 200)

    def tearDown(self):
        pygame.quit()

    def test_ball_bounce_wall(self):
        self.ball.rect.x = 0
        self.ball.speed_x = -4
        self.ball.update(self.brick_group, self.screen_rect)
        self.assertEqual(self.ball.speed_x, 4)

    def test_ball_bounce_brick(self):
        self.ball.rect.x = self.brick.rect.x
        self.ball.rect.y = self.brick.rect.y - self.ball.radius * 2
        self.ball.speed_y = 4
        self.ball.update(self.brick_group, self.screen_rect)
        self.assertEqual(self.ball.speed_y, -4)

if __name__ == "__main__":
    unittest.main()

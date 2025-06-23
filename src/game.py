import pygame

from brick import Brick


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pygame 기본 창")
        self.WHITE = (255, 255, 255)
        self.running = True
        # Brick 인스턴스 생성
        self.brick = Brick(x=270, y=190)
        self.all_sprites = pygame.sprite.Group(self.brick) #type:ignore[no-redef]

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                        self.running = False
                    if event.key == pygame.K_q and (event.mod & pygame.KMOD_SHIFT):
                        self.running = False
            keys = pygame.key.get_pressed()
            self.all_sprites.update(keys)
            self.screen.fill(self.WHITE)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)

import pygame

from pygame.locals import (
    K_UP,
    K_DOWN, 
    K_w,
    K_s
)

class Block(pygame.sprite.Sprite):
    def __init__(self, SCREENWIDTH, SCREEN_HEIGHT, isPlayer1 = True):
        super(Block, self).__init__()
        self.sw = SCREENWIDTH
        self.sh = SCREEN_HEIGHT
        self.surf = pygame.Surface((25,200))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (
                12.5 if isPlayer1 else self.sw - 12.5, 300
            )
        )
        self.ip1 = isPlayer1



    def update(self, pressed_keys):
        if pressed_keys[K_UP] and not self.ip1:
            self.rect.move_ip(0, -5)

        if pressed_keys[K_DOWN] and not self.ip1:
            self.rect.move_ip(0, 5)
        
        if pressed_keys[K_w] and self.ip1:
            self.rect.move_ip(0, -5)

        if pressed_keys[K_s] and self.ip1:
            self.rect.move_ip(0, 5)

        # Keep player on the screen

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.sw:
            self.rect.right = self.sw
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.sh:
            self.rect.bottom = self.sh

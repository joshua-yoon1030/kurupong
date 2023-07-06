import pygame
import random
class Ball(pygame.sprite.Sprite):
    def __init__(self, SCREENWIDTH, SCREEN_HEIGHT):
        super(Ball, self).__init__()
        self.sw = SCREENWIDTH
        self.sh = SCREEN_HEIGHT
        self.images = [pygame.image.load("img/hertaa_1.png"),
                       pygame.image.load("img/hertaa_2.png"),
                       pygame.image.load("img/hertaa_3.png"),
                       pygame.image.load("img/hertaa_4.png"),
                       pygame.image.load("img/hertaa_5.png"),
                       pygame.image.load("img/hertaa_6.png")
                       ]
        self.index = 0
        self.surf = pygame.image.load("img/hertaa_1.png")
        self.rect = self.surf.get_rect(
            center = (
                SCREENWIDTH/2, SCREEN_HEIGHT/2
            )
        )
        self.vx = 5 if random.randint(1, 2) % 2 == 0 else -5
        self.vy = 5 if random.randint(1, 2) % 2 == 0 else -5
        self.kuru1 = pygame.mixer.Sound("sfx/kuru1.ogg")
        self.kuru2 = pygame.mixer.Sound("sfx/kuru2.ogg")
    def update(self):
        self.rect.move_ip(self.vx, self.vy)

        # Keep player on the screen

        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = 0
            return -1
        if self.rect.right > self.sw:
            self.rect.right = self.sw
            self.vx = 0
            return 1
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vy = -self.vy
            self.makeNoise()
        if self.rect.bottom >= self.sh:
            self.rect.bottom = self.sh
            self.vy = -self.vy
            self.makeNoise()
            

        self.surf = self.images[self.index % len(self.images)]
        self.index += 1
        
        return 0
    def makeNoise(self):
        if random.randint(1, 2) % 2 == 0:
            pygame.mixer.Sound.play(self.kuru1)
        else:
            pygame.mixer.Sound.play(self.kuru2)
    def speedUp(self):
        if self.vx < 0:
            self.vx -= 2
        else:
            self.vx += 2
        if self.vy < 0:
            self.vy -= 2
        else:
            self.vy += 2
    def reset(self):
        self.rect = self.surf.get_rect(
            center = (
                self.sw/2, self.sh/2
            )
        )
        self.vx = 5 if random.randint(1, 2) % 2 == 0 else -5
        self.vy = 5 if random.randint(1, 2) % 2 == 0 else -5
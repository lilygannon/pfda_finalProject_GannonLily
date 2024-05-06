import pygame
import random

WIDTH = 1080
HEIGHT = 580


class Rain(pygame.sprite.Sprite):
    def __init__(self, rain_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img
        self.rect = self.image.get_rect()
        self.speedx = 3
        self.speedy = random.randint(5, 25)
        self.rect.x = random.randint(-100, WIDTH)
        self.rect.y = random.randint(-HEIGHT, -5)

    def update(self):

        if self.rect.bottom > HEIGHT:
            self.speedx = 3
            self.speedy = random.randint(5, 25)
            self.rect.x = random.randint(-HEIGHT, WIDTH)
            self.rect.y = random.randint(-HEIGHT, -5)

        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
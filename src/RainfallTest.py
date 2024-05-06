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


def main():
    pygame.init()

    clock = pygame.time.Clock()

    bg_color = (52, 69, 76)

    rain_img = pygame.image.load('src/Raindrop.png')

    wn = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Torrential Rain')

    rain_group = pygame.sprite.Group()

    for i in range(100):
        rain = Rain(rain_img)
        rain_group.add(rain)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        rain_group.update()

        wn.fill(bg_color)
        rain_group.draw(wn)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()

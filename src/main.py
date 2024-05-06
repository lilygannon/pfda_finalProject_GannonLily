import pygame
import pygame.freetype
from RainfallTest import Rain
from random import randint
from sys import exit

WIDTH = 1080
HEIGHT = 580

def main():
    pygame.init()

    clock = pygame.time.Clock()

    bg_color = (52, 69, 76)

    rain_img = pygame.image.load('Raindrop.png')

    wn = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Rain or Snow')

    rain_group = pygame.sprite.Group()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    GAME_FONT = pygame.freetype.Font("Harmond-SemBdItaCond.otf", 24)
    running = True

    screen.fill((0, 0, 0))
    text_surface, rect = GAME_FONT.render("Welcome to Rain or Snow!", (255, 255, 255))
    screen.blit(text_surface, (WIDTH/2.5, HEIGHT/2.5))
    text_surface, rect = GAME_FONT.render("For rainfall press 'r' and for snow press 's'.", (255, 255, 255))
    screen.blit(text_surface, (WIDTH/3, HEIGHT/2))
    text_surface, rect = GAME_FONT.render("To escape press 'esc'.", (255, 255, 255))
    screen.blit(text_surface, (WIDTH/2.5, HEIGHT/1.70))
    text_surface, rect = GAME_FONT.render("Have fun!", (255, 255, 255))
    screen.blit(text_surface, (WIDTH/2.25, HEIGHT/1.5))

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    for i in range(50):
                        rain = Rain(rain_img)
                        rain_group.add(rain)
                        rain_group.update()

                        wn.fill(bg_color)
                        rain_group.draw(wn)
                        pygame.display.flip()
                        clock.tick(50)
                '''elif event.key == pygame.K_s:
                        '''
            elif event.type == pygame.QUIT:
                running = False
                    


        


if __name__ == "__main__":
    main()
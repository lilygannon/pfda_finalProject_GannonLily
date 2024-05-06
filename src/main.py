import pygame
import pygame.freetype
from Rainfall import Rain
from Snowfall import Snowflake
from random import randint

WIDTH = 1080
HEIGHT = 580


def main():
    pygame.init()

    clock = pygame.time.Clock()

    bg_color = (52, 69, 76)

    rain_img = pygame.image.load('Raindrop.png')

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Rain or Snow')

    rain_group = pygame.sprite.Group()

    trees_back = pygame.image.load('trees_back.png').convert_alpha()
    trees_front = pygame.image.load('trees_front.png').convert_alpha()
    game_font = pygame.freetype.Font("Harmond-SemBdItaCond.otf", 24)
    running = True

    screen.fill((0, 0, 0))
    text_surface, rect = game_font.render("Welcome to Rain or Snow!", 
                                          (255, 255, 255))
    screen.blit(text_surface, (WIDTH/2.5, HEIGHT/2.5))
    text_surface, rect = game_font.render("For rainfall press 'r' and for snow"
                                          " press 's'.", (255, 255, 255))
    screen.blit(text_surface, (WIDTH/3, HEIGHT/2))
    text_surface, rect = game_font.render("To escape press 'esc'.", 
                                          (255, 255, 255))
    screen.blit(text_surface, (WIDTH/2.5, HEIGHT/1.70))
    text_surface, rect = game_font.render("Have fun!", (255, 255, 255))
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

                        screen.fill(bg_color)
                        rain_group.draw(screen)
                        pygame.display.flip()
                        clock.tick(50)
                elif event.key == pygame.K_s:
                    snowflakes = []
                    for i in range(0, 500):
                        position = (randint(0, WIDTH), randint(0, HEIGHT))
                        gravity = randint(1, 2)
                        radius = randint(2, 4)
                        snowflakes.append(Snowflake(position, radius, gravity))

                        screen.blit(trees_back, (0, 0))	

                        for snowflake in snowflakes:
                            pygame.draw.circle(screen, snowflake.color, 
                                               snowflake.pos, snowflake.radius)
                            snowflake.controller(HEIGHT, WIDTH)

                        screen.blit(trees_front, (0, 0))	

                        pygame.display.update()
                        clock.tick(30)
            elif event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

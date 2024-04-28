import pygame
from random import randint
from sys import exit


class Snowflake:
	def __init__(self, position, radius, gravity):
		self.pos = position
		self.radius = radius
		self.gravity = gravity
		self.RADIUS_MAX = radius
		self.radius_change = True
		self.color = (255, 255, 255)

	def controller(self, height, width):
		self.update_pos(height, width)
		self.update_rad()
		self.update_color(height)

	def update_pos(self, height, width):
		if self.pos[1] < height + self.radius:
			self.pos = (self.pos[0] + randint(-1, 1), self.pos[1] + self.gravity)
		else:
			self.respawn(width)

	def update_rad(self):
		if self.radius_change:
			self.radius = randint(1, self.RADIUS_MAX)
			self.radius_change = False
		else:
			self.radius_change = True

	def update_color(self, height):
		rgb = 250 - 100 * (self.pos[1] / height) 
		self.color = (rgb, rgb, rgb)

	def respawn(self, width):
	 	self.pos = (randint(0, width), -1 * self.radius)


def main():
	pygame.init()
	WIDTH, HEIGHT = 1080, 580
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Snow Simulation")
	clock = pygame.time.Clock()

	snowflakes = []
	for i in range(0, 500):
		position = (randint(0, WIDTH), randint(0, HEIGHT))
		gravity = randint(1, 2)
		radius = randint(2, 4)
		snowflakes.append(Snowflake(position, radius, gravity))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		for snowflake in snowflakes:
			pygame.draw.circle(screen, snowflake.color, snowflake.pos, snowflake.radius)
			snowflake.controller(HEIGHT, WIDTH)

		pygame.display.update()
		clock.tick(30)
	

if __name__ == "__main__":
	main()
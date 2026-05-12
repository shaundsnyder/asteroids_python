from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position +=  self.velocity * dt

	def split(self):
		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		log_event("asteroid_split")
		angle = random.uniform(20, 50)

		asteroid_1_velocity = self.velocity.rotate(angle)
		asteroid_2_velocity = self.velocity.rotate(-angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

		new_asteroid_1.velocity = asteroid_1_velocity * 1.2
		new_asteroid_2.velocity = asteroid_2_velocity * 1.2

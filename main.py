import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot


def main():
	pygame.init()
	game_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, drawable, updatable)

	asteroidfield = AsteroidField()
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT /2)


	#Print Config Details
	print(f"Starting Asteroids with pygame version: {pygame.version.vernum}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


	#Game Loop

	while True:
		log_state()
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				 return

		screen.fill((0, 0, 0))
		updatable.update(dt)
		for d in drawable:
			d.draw(screen)
		pygame.display.flip()

		for asteroid in asteroids:
			if player.collides_with(asteroid):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
			for s in shots:
				if s.collides_with(asteroid):
					log_event("asteroid_shot")
					s.kill()
					asteroid.split()

		time_passed = game_clock.tick(60)
		dt = time_passed / 1000


if __name__ == "__main__":
    main()

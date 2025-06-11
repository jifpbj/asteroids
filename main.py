import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = ( updatable, drawable )
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    asteroid_field = AsteroidField()
### Game Loop ###
    while True:
        ### close window and quit### 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        updatable.update(dt)

        # Handle collision (e.g., end game, reduce health, etc.)
        for asteroid in asteroids:
            if asteroid.detect_collisions(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.detect_collisions(shot):
                    shot.kill()
                    asteroid.split(ASTEROID_MIN_RADIUS)

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() # update contents of the display
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()


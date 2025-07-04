import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updateable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                return sys.exit("Game over!")
            for shot in shots:
                if asteroid.collision(shot) == True:
                    asteroid.split()
                    shot.kill()
        screen.fill((0,0,0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)
        dt /= 1000
        
    
if __name__ == "__main__":
    main()

import sys
import pygame
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
    
    # object groups
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x , y)

    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill( "black" ) # can use str "black" or (0,0,0)

        #player.update(dt)
        #player.draw(screen)
        updatable.update(dt)

        for item in drawable:
            item.draw(screen)

        for item in asteroids:
            if item.iscollided_with(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        
        # pause the loop for 1/60 sec
        time_passed = clock.tick(60)
        dt = time_passed / 1000 # dt in seconds


if __name__ == "__main__":
    main()

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

    font = pygame.font.Font(None, 24)
    text_color = ["red", "red", "orange", "green"]
    game_over_font = pygame.font.Font(None, 60)
    
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

        text = font.render(f"Lives: {player.lives}", True, text_color[player.lives])
        textpos = text.get_rect(x=12,y=12)
        screen.blit(text, textpos)
        
        if player.lives < 1:
            game_over = game_over_font.render("GAME OVER", True, 'red')
            screen.blit(game_over, game_over.get_rect(centerx=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2))


        updatable.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.iscollided_with(player):
                if player.lives < 2:
                    player.kill()
                    #print("Game over!")
                    #sys.exit()
                asteroid.kill()
                player.lives = max([0, player.lives - 1])

            for bullet in shots:
                if bullet.iscollided_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        pygame.display.flip()
        
        # pause the loop for 1/60 sec
        time_passed = clock.tick(60)
        dt = time_passed / 1000 # dt in seconds


if __name__ == "__main__":
    main()

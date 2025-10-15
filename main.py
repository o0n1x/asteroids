from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    
    #player
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    #game loop
    while True:
        #handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        #deltatime
        dt = clock.tick(60) / 1000.0

        #controls
        updatable.update(dt)


        #display
        screen.fill("black")   

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #game logic

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return
            
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()


if __name__ == "__main__":
    main()

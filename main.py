from constants import *
from player import Player
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    #player
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    #game loop
    while True:
        #handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        #controls
        player.update(dt)


        #display
        screen.fill("black")   
        player.draw(screen) 

        pygame.display.flip()

        #deltatime
        dt = clock.tick(60)

if __name__ == "__main__":
    main()

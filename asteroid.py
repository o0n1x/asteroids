from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        velo1 = self.velocity
        velo2 = self.velocity
        velo1 = velo1.rotate(random_angle)
        velo2 = velo2.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0],self.position[1],radius)
        asteroid2 = Asteroid(self.position[0],self.position[1],radius)
        asteroid1.velocity = velo1 * 1.2
        asteroid2.velocity = velo2 * 1.2
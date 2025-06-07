import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_pos = pygame.math.Vector2.rotate(self.velocity, angle)
        new_neg = pygame.math.Vector2.rotate(self.velocity, -angle)
        pos_rad = self.radius - ASTEROID_MIN_RADIUS
        neg_rad = self.radius - ASTEROID_MIN_RADIUS
        pos_new = Asteroid(self.position[0], self.position[1], pos_rad)
        pos_new.velocity = new_pos * 1.2
        neg_new = Asteroid(self.position[0], self.position[1], neg_rad)
        neg_new.velocity = new_neg * 1.2
        return pos_new, neg_new
        
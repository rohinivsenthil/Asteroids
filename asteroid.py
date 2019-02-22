import random
import math

import pygame
from pygame.locals import *


def linspace(start, stop, num_steps):
    values = []
    delta = (stop - start) / num_steps
    for i in range(num_steps):
        values.append(start + i * delta)
    return values


def generate_polygon(center, mu, sigma, maxr, num_points):
    points = []

    for theta in linspace(0, 2*math.pi - (2*math.pi/num_points), num_points):
        radius = min(random.gauss(mu, sigma), maxr)
        x = center[0] + radius * math.cos(theta)
        y = center[1] + radius * math.sin(theta)
        points.append([x, y])

    return points


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, radius, speed, pos):
        super().__init__()

        points = generate_polygon(
            (radius, radius),
            radius - (radius / 5),
            (radius / 10),
            radius,
            random.randint(10, 20)
        )

        self.image = pygame.Surface(
            (radius * 2, radius * 2),
            SRCALPHA,
            32
        )

        pygame.draw.polygon(self.image, pygame.Color(0, 0, 255), points, 2)

        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.pos = list(pos)
        self.speed = speed

    def update(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        self.rect.center = self.pos


from pygame import Rect
from pygame import Color
from random import random

class Particle():

    def __init__(self, x, y, vx, vy, s, duration):
        self._duration = duration
        self._life = duration
        self._x = x
        self._y = y
        self._size = s
        self._vx = randomRange(-vx, vx)
        self._vy = randomRange(-vy, vy)
        self._baseColor = (255, 0, 0)

    def update(self, dt):
        if self._life > 0:
            self._life -= dt
            # alpha = 255 * (self._life / self._duration)
            self._color = self._baseColor
            # self._color.a = alpha
            self._x = self._x + self._vx * dt
            self._y = self._y + self._vy * dt
            self._rect = Rect(self._x, self._y, 1, 1)
        pass

    def draw(self, screen):
        if self._life > 0:
            print("vx {0}".format(self._vx))
            print("x {0}".format(self._rect.x))
            screen.draw.filled_rect(self._rect, self._baseColor)

class ParticleEngine():

    _particles = []

    def __init__(self, maxParticles):
        self.maxParticles = maxParticles
        for n in range(0, self.maxParticles):
            particle = Particle(100, 100, randomRange(20, 51), randomRange(20, 51), 5, randomRange(2, 5))
            self._particles.append(particle)

    def emit(self, count, x, y):
        pass

    def update(self, dt):
        for particle in self._particles:
            particle.update(dt)

    def draw(self, screen):
        for particle in self._particles:
            particle.draw(screen)


def randomRange(min, max):
    value = random()
    scaled = min + (value * (max - min))
    print(scaled)
    return scaled
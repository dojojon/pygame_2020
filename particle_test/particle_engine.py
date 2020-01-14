from pygame import Rect
from pygame import Color
from random import random
from random import randint

color_sets = {
    "red": [
        (255, 0, 0)
    ],
    "green": [
        (0, 255, 0)
    ],
    "blue": [
        (0, 0, 255)
    ],
    "christmas": [
        (0, 255, 0),
        (255, 0, 0)
    ]
}


class Particle():

    def __init__(self, x, y, vx, vy, s, duration=5, color=(255, 255, 255)):
        self._duration = duration
        self._life = duration
        self._x = x
        self._y = y
        self._size = s
        self._vx = randomRange(-vx, vx)
        self._vy = randomRange(-vy, vy)
        self._baseColor = color

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
            # print("vx {0}".format(self._vx))
            # print("x {0}".format(self._rect.x))
            screen.draw.filled_rect(self._rect, self._baseColor)

    def alive(self):
        return self._life > 0

class ParticleEngine():

    _particles = []

    def __init__(self):
        pass

    def emit(self, x, y, count=20, colors=[(255, 0, 0)]):
        for n in range(0, count):
            vx = randomRange(20, 51)
            vy = randomRange(20, 51)
            size = 5
            color = randomColor(colors)
            duration = 5
            particle = Particle(x, y, vx, vy, size, duration, color)

            self._particles.append(particle)

    def update(self, dt):

        # update particles
        for particle in self._particles:
            particle.update(dt)

        # remove any dead particles
        self._particles = [x for x in self._particles if x.alive()]
        print("Alve {0}".format(len(self._particles)))


    def draw(self, screen):
        for particle in self._particles:
            particle.draw(screen)


def randomRange(min, max):
    value = random()
    scaled = min + (value * (max - min))
    return scaled


def randomColor(colors):
    maxIndex = len(colors) - 1
    index = randint(0, maxIndex)
    return colors[index]
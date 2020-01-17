from pygame import Rect
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


def randomRange(min, max):
    value = random()
    scaled = min + (value * (max - min))
    return scaled


def randomColor(colors):
    maxIndex = len(colors) - 1
    index = randint(0, maxIndex)
    return colors[index]


class Emitter():

    def __init__(self, position, vx, vy, size, volume, emit_duration, duration, colors=color_sets["red"]):
        self._duration = duration

        self._position = position
        self._vx = vx
        self._vy = vy
        self._size = size
        self._volume = volume
        self._emit_duration = emit_duration
        self._duration = duration
        self._colors = colors

    def emit(self, dt):
        emitted = []
        # self._emit_duration += -dt
        for n in range(0, self._volume):
            color = randomColor(self._colors)
            vx = randomRange(int(self._vx[0]), int(self._vx[1]))
            vy = randomRange(int(self._vy[0]), int(self._vy[1]))
            x = self._position[0]
            y = self._position[1]
            particle = Particle(x, y, vx, vy, self._size, self._duration, color)

            emitted.append(particle)

        return emitted

    def alive(self):
        return False  #` self._emit_duration > 0

class Particle():

    def __init__(self, x, y, vx, vy, size=2, duration=5, color=(255, 255, 255)):
        self._duration = duration
        self._life = duration
        self._x = x
        self._y = y
        self._size = size
        self._vx = vx
        self._vy = vy
        self._baseColor = color

    def update(self, dt):
        if self._life > 0:
            self._life -= dt
            # alpha = 255 * (self._life / self._duration)
            self._color = self._baseColor
            # self._color.a = alpha
            self._x = self._x + self._vx * dt
            self._y = self._y + self._vy * dt
            self._rect = Rect(self._x, self._y, self._size, self._size)
        pass

    def draw(self, screen):
        if self._life > 0:
            # print("vx {0}".format(self._vx))
            # print("x {0}".format(self._rect.x))
            screen.draw.filled_rect(self._rect, self._baseColor)

    def alive(self):
        return self._life > 0

class ParticleEngine():

    _emitters = []
    _particles = []

    def __init__(self):
        pass

    def emit(self, position, size=2, volume=20, colors=color_sets["red"], emit_duration=-1, duration=1):
        emitter = Emitter(position, (-20, 20), (-20, 20), size, volume, emit_duration, duration, colors)
        self._emitters.append(emitter)
        pass

    def update(self, dt):

        # Update emitters
        for emitter in self._emitters:
            self._particles += emitter.emit(dt)

        self._emitters = [x for x in self._emitters if x.alive()]

        # update particles
        for particle in self._particles:
            particle.update(dt)

        # remove any dead particles
        self._particles = [x for x in self._particles if x.alive()]
        # print("Alve {0}".format(len(self._particles)))

    def draw(self, screen):
        for particle in self._particles:
            particle.draw(screen)

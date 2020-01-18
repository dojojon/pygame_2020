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
    "rgb": [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255)
    ],
    "christmas": [
        (0, 255, 0),
        (255, 0, 0)
    ],
    "juice":[
        (255, 244, 79),
        (255, 255, 255),
        (50, 205, 50)
    ]
}

effects = {

    "juice": {
        "size": 2,
        "volume": 2,
        "colors": color_sets["juice"],
        "emit_duration": 1.5,
        "duration": 0.75
    }
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

    def __init__(self, position, config):
        self.position = config["position"]
        self.vx = config["vx"]
        self.vy = config["vy"]
        self.size = config["size"]
        self.volume = config["volume"]
        self.emit_duration = config["emit_duration"]
        self.duration = config["duration"]
        self.colors = config["colors"]

    def emit(self, dt):
        emitted = []
        self.emit_duration += -dt
        for n in range(0, self.volume):
            color = randomColor(self.colors)
            vx = randomRange(int(self.vx[0]), int(self.vx[1]))
            vy = randomRange(int(self.vy[0]), int(self.vy[1]))
            x = self.position[0]
            y = self.position[1]
            particle = Particle(x, y, vx, vy, self.size, self.duration, color)

            emitted.append(particle)

        return emitted

    def alive(self):
        return self.emit_duration > 0


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

    def emit(self, position, config=None, vx=(-20, 20), vy=(-20,20), size=None, volume=None, colors=color_sets["red"], emit_duration=None, duration=None):
      
        em_config = {
            "position":position, 
            }

        if config is not None:
            em_config = {** config}

        if size is not None:
            em_config["size"] = size
        else:
            em_config["size"] = 2

        if volume is not None:
            em_config["volume"] = volume
        else:
            em_config["volume"] = 5

        if colors is not None:
            em_config["colors"] = colors
        else:
            em_config["colors"] = color_sets["rgb"]

        if emit_duration is not None:
            em_config["emit_duration"] = emit_duration
        else:
            em_config["emit_duration"] = -1

        if duration is not None:
            em_config["duration"] = duration
        else:
            em_config["duration"] = 3

        if vx is not None:
            em_config["vx"] = vx
        else:
            em_config["vx"] = (-25, 25)
            
        if vy is not None:
            em_config["vy"] = vy
        else:
            em_config["vy"] = (-25, 25)

        emitter = Emitter(position, em_config)
        self._emitters.append(emitter)
        return emitter

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

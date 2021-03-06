from pygame import Rect
from random import random
from random import randint
import math

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
    "ice": [
        (0, 0, 255),
        (255, 255, 255),
        (50, 50, 255)
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
    "juice": [
        (255, 244, 79),
        (255, 255, 255),
        (50, 205, 50)
    ],
    "fire": [
        (255, 0, 0),
        (255, 165, 0),
        (250, 205, 0)
    ],
    "smoke":[
        (150,140,180),
        (180,160,160),
        (130,120,160)
    ]
}

effects = {

    "juice": {
        "size": 2,
        "volume": 2,
        "vx": (-20, 20),
        "vy": (-20, 20),
        "colors": color_sets["juice"],
        "emit_duration": .5,
        "duration": 0.75,
    },
    "shockWave": {
        "colors": color_sets["fire"],
        "emit_duration": .125,
        "volume": 100,
        "size": 2,
        "duration": .75,
        "vx": (-80, 80),
        "vy": (-80, 80),
        "vMax": 60,
        "vMin": 30
    },
    "jet": {
        "colors": color_sets["fire"],
        "emit_duration": .025,
        "volume": 2,
        "size": 3,
        "duration": .75,
        "angle": 0,
        "angleSpread": 8,
        "vMax": 100,
        "vMin": 90
    },
    "smoke": {
        "colors": color_sets["smoke"],
        "emit_duration": 0,
        "volume": 1,
        "size": 9,
        "duration": 10,
        "angle": 180,
        "angleSpread": 30,
        "vMax": 20,
        "vMin": 15
    }
}


def valueOrDefault(key, dictionay, default):
    if key in dictionay:
        return dictionay[key]
    else:
        return default


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
        self.position = position

        self.vMin = valueOrDefault("vMin", config, -1)
        self.vMax = valueOrDefault("vMax", config, 9999)

        if "angle" in config and  config["angle"] is not None:
            angle = config["angle"]
            minAngle = angle - valueOrDefault("angleSpread",config, 90)
            maxAngle = angle + valueOrDefault("angleSpread",config, 90)

            self.vx = (math.sin(math.radians(minAngle)) * randomRange(self.vMin,  self.vMax),
                               math.sin(math.radians(maxAngle)) * randomRange(self.vMin,  self.vMax))

            self.vy =  (math.cos(math.radians(minAngle)) * randomRange(self.vMin,  self.vMax),
                               math.cos(math.radians(maxAngle)) * randomRange(self.vMin,  self.vMax))
        else:
            self.vx = valueOrDefault("vx", config, (-20, 20))
            self.vy = valueOrDefault("vy", config, (-20, 20))

 
        self.size = valueOrDefault("size", config, 3)
        self.volume = valueOrDefault("volume", config, 10)
        self.emit_duration = valueOrDefault("emit_duration", config, -1)
        self.duration = valueOrDefault("duration", config, 3)
        self.colors = valueOrDefault("colors", config, color_sets["rgb"])

    def emit(self, dt):
        emitted = []
        self.emit_duration += -dt
        for n in range(0, self.volume):
            color = randomColor(self.colors)
            vx = randomRange(int(self.vx[0]), int(self.vx[1]))
            vy = randomRange(int(self.vy[0]), int(self.vy[1]))
            x = self.position[0]
            y = self.position[1]
            particle = Particle(x, y, vx, vy, self.vMin,
                                self.vMax, self.size, self.duration, color)

            emitted.append(particle)

        return emitted

    def alive(self):
        return self.emit_duration > 0


class Particle():

    def __init__(self, x, y, vx, vy, vMin=None, vMax=None, size=2, duration=5, color=(255, 255, 255)):
        self._duration = duration
        self._life = duration
        self._x = x
        self._y = y
        self._size = size
        self._vx = vx
        self._vy = vy
        self._baseColor = color
        self._vMin = vMin
        self._vMax = vMax

    def update(self, dt):
        if self.alive():
            self._life -= dt
            # alpha = 255 * (self._life / self._duration)
            self._color = self._baseColor
            # self._color.a = alpha
            self._x = self._x + self._vx * dt
            self._y = self._y + self._vy * dt
            self._rect = Rect(self._x, self._y, self._size, self._size)
        pass

    def draw(self, screen):
        if self.alive():
            screen.draw.filled_rect(self._rect, self._baseColor)

    def alive(self):
        velocityCull = False
        if self._vMin is not None or self._vMin is not None:
            velocity = (self._vx**2 + self._vy**2)**0.5
            if self._vMin is not None and self._vMin > velocity:
                velocityCull = True
            elif self._vMax is not None and self._vMax < velocity:
                velocityCull = True

        return velocityCull is False and self._life > 0


class ParticleEngine():

    _emitters = []
    _particles = []

    def __init__(self):
        pass

    def emit(self, position, config=None, angle=None, angleSpread=None, vx=None, vy=None, vMin=None, vMax=None, size=None, volume=None, colors=None, emit_duration=None, duration=None):

        em_config = {
            "position": position,
        }

        if config is not None:
            em_config = {**config}

        if size is not None:
            em_config["size"] = size

        if volume is not None:
            em_config["volume"] = volume

        if colors is not None:
            em_config["colors"] = colors

        if emit_duration is not None:
            em_config["emit_duration"] = emit_duration

        if duration is not None:
            em_config["duration"] = duration

        if vx is not None:
            em_config["vx"] = vx

        if vy is not None:
            em_config["vy"] = vy

        if vMin is not None:
            em_config["vMin"] = vMin

        if vMax is not None:
            em_config["vMax"] = vMax

        if angleSpread is not None:
            em_config["angleSpread"] = angleSpread

        if angle is not None:
            em_config["angle"] = angle

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

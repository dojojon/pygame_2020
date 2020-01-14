import pgzrun
from random import randint
from particle_engine import ParticleEngine

WIDTH = 800
HEIGHT = 600

pe = ParticleEngine()


def update(dt):

    pe.update(dt)
    pass


colors = [(123, 123, 0), (0, 123, 23), (0, 30, 90)]


def on_key_down(key):
    if key == keys.SPACE:
        s = 100
        x = randint(s, WIDTH - (2 * s))
        y = randint(s, HEIGHT - (2 * s))
        pe.emit(x, y, 50, colors)


def draw():

    screen.clear()
    s = 100
    rect = Rect(s, s, WIDTH - 2 * s, HEIGHT- 2 * s)
    screen.draw.rect(rect, (255, 255, 0))
    pe.draw(screen)
    # pass 


pgzrun.go()
import pgzrun
from random import randint
from particle_engine import ParticleEngine
from particle_engine import color_sets, effects

WIDTH = 800
HEIGHT = 600
jet_angle = 0

pe = ParticleEngine()

def update(dt):
    juice()
    jet()
    smoke()

    pe.update(dt)


def on_key_down(key):
    if key == keys.SPACE:
        boom()
        juice()
    
    if key == keys.J:
        jet()


def smoke():
    pe.emit((120, HEIGHT- 180),config=effects["smoke"])


def jet():
    global jet_angle

    jet_angle += 1
    if jet_angle > 360:
        jet_angle = 0

    x = WIDTH  / 2
    y = 200
    pe.emit((x, y), config=effects["jet"], colors=color_sets["rgb"], angle=jet_angle, angleSpread=20)


def juice():
    s = 100
    x = randint(s, WIDTH - s)
    y = randint(s, HEIGHT - s)
    pe.emit((x, y), config=effects["juice"], emit_duration=.25)


def boom():
    x =  WIDTH / 2
    y = HEIGHT / 2
    pe.emit((x, y), config=effects["shockWave"])


def draw():

    screen.clear()
    s = 100
    rect = Rect(s, s, WIDTH - 2 * s, HEIGHT- 2 * s)
    screen.draw.rect(rect, (255, 255, 0))
    pe.draw(screen)
    # pass 


pgzrun.go()
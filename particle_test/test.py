import pgzrun
from random import randint
from particle_engine import ParticleEngine

WIDTH = 600
HEIGHT = 400

pe = ParticleEngine()


def update(dt):
    pe.update(dt)
    pass

def on_key_down(key):
    if key == keys.SPACE:
        pe.emit(25, randint(10, WIDTH-10), randint(10,HEIGHT-10))

def draw():

    screen.clear()

    pe.draw(screen)
    # pass 


pgzrun.go()
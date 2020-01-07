import pgzrun
# from random import randint
from particle_engine import ParticleEngine

WIDTH = 600
HEIGHT = 400

pe = ParticleEngine(50)


def update(dt):
    pe.update(dt)
    pass


def draw():

    screen.clear()

    pe.draw(screen)
    # pass 


pgzrun.go()
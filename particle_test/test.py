import pgzrun
from random import randint
from particle_engine import ParticleEngine
from particle_engine import color_sets

WIDTH = 800
HEIGHT = 600

pe = ParticleEngine()


def update(dt):
    juice()
    pe.update(dt)
    pass

def on_key_down(key):
    if key == keys.SPACE:
        boom()

def juice():
    s = 100
    x = randint(s, WIDTH - s)
    y = randint(s, HEIGHT - s)
    pe.emit((x, y),colors=color_sets["juice"])

def boom():
    x =  WIDTH / 2
    y = HEIGHT / 2
    pe.emit((x, y),colors=color_sets["fire"], emit_duration=2, volume=100, duration=0.75)
  
def draw():

    screen.clear()
    s = 100
    rect = Rect(s, s, WIDTH - 2 * s, HEIGHT- 2 * s)
    screen.draw.rect(rect, (255, 255, 0))
    pe.draw(screen)
    # pass 


pgzrun.go()
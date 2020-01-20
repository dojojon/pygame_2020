import pgzrun
import pygame
from random import randrange
from common.particle_engine import ParticleEngine, effects

WIDTH=800
HEIGHT=600
PLAYER_SPEED = 5
LASER_SPEED = 8
TIE_SPEED_RANGE = (5, 8)

clock = pygame.time.Clock()

pe = ParticleEngine()

player = Actor('falcon')
player.x = WIDTH/2
player.y = HEIGHT/2

lasers = []
fighters = []

for _ in range(0, 10):
    x  = randrange(WIDTH, WIDTH*2)
    y  = randrange(20, HEIGHT - 20)
    tie = Actor('tie')
    tie.left = x
    tie.top = y
    tie.speed =randrange(TIE_SPEED_RANGE[0], TIE_SPEED_RANGE[1])

    fighters.append(tie)

def update(dt):
    global lasers

    pe.update(dt)

    update_player(dt)

    for laser in lasers:
        laser.right += LASER_SPEED

    lasers =[x for x in lasers if laser.left < WIDTH]
        
    for tie in fighters:
        tie.right -= tie.speed

        if tie.right < 0:
            
            reset_tie(tie)
        
        else:

            for laser in lasers:
                if laser.colliderect(tie):
                    pe.emit((laser.x, laser.y), config=effects["shockWave"], volume=10, emit_duration=0.124)
                    reset_tie(tie)
    pass

def reset_tie(tie):
    x  = WIDTH + randrange(0, 100)
    y  = randrange(20, HEIGHT - 20)
    tie.left = x
    tie.top = y
    tie.alive = True

def update_player(dt):
    global lasers

    if keyboard.up:
        player.top -= PLAYER_SPEED
    if keyboard.down:
        player.top += PLAYER_SPEED
    if keyboard.left:
        player.left -= PLAYER_SPEED
    if keyboard.right:
        player.left += PLAYER_SPEED

    if keyboard.space and len(lasers) < 10:
        laser = Actor('laser')
        laser.left = player.right
        laser.top = player.top
        lasers.append(laser)

def draw():
    screen.fill((0, 10, 30))
    player.draw()

    clock.tick()
    screen.draw.text(str(clock.get_fps()), (20,20))

    for laser in lasers:
        laser.draw()
    
    for tie in fighters:
        tie.draw()
    
    pe.draw(screen)


pgzrun.go()

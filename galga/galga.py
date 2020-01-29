import pgzrun
import pygame
from random import randrange
from common.particle_engine import ParticleEngine, effects

WIDTH=800
HEIGHT=600
PLAYER_SPEED = 200
LASER_SPEED = 250
TIE_SPEED_RANGE = (200, 500)

pe = ParticleEngine()

player = Actor('falcon')
player.x = WIDTH/2
player.y = HEIGHT/2

lives = 3

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
    global lasers, lives

    pe.update(dt)

    if lives > 0:
        update_player(dt)

        update_ties(dt)
    
        update_lasers(dt)


def reset_tie(tie):
    x  = WIDTH + randrange(0, 100)
    y  = randrange(20, HEIGHT - 20)
    tie.left = x
    tie.top = y
    tie.alive = True


def update_ties(dt):
    global fighters, lives

    for tie in fighters:

        tie.right -= tie.speed  * dt

        if tie.colliderect(player):
            reset_tie(tie)
            pe.emit((player.x, player.y), config=effects["shockWave"], volume=10, emit_duration=0.124)
            lives -= 1            

        if tie.right < 0:
            reset_tie(tie)
    
        for laser in lasers:
            if laser.colliderect(tie):
                pe.emit((laser.x, laser.y), config=effects["shockWave"], volume=10, emit_duration=0.124)
                laser.alive = False
                reset_tie(tie)


def update_lasers(dt):
    global lasers

    for laser in lasers:
        laser.right += LASER_SPEED  * dt
    
    lasers =[x for x in lasers if (laser.left < WIDTH and laser.alive == True)]

        

def update_player(dt):
    global lasers

    if keyboard.up:
        player.top -= PLAYER_SPEED * dt
    if keyboard.down:
        player.top += PLAYER_SPEED  * dt
    if keyboard.left:
        player.left -= PLAYER_SPEED  * dt
    if keyboard.right:
        player.left += PLAYER_SPEED  * dt

    if keyboard.space and len(lasers) < 1:
        laser = Actor('laser')
        laser.left = player.right
        laser.top = player.top
        laser.alive = True
        lasers.append(laser)


def draw():
    screen.fill((0, 10, 30))
    player.draw()

    screen.draw.text("Lives: {0}".format(lives), (20, 20))
    
    for laser in lasers:
        laser.draw()
    
    for tie in fighters:
        tie.draw()
    
    pe.draw(screen)

    if lives <= 0:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), color=(255,0,0), fontsize=180 )


pgzrun.go()

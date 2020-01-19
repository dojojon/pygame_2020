import pgzrun
from random import randint
from common.particle_engine import ParticleEngine, color_sets, effects

WIDTH = 600
HEIGHT = 400

PLAYER_SPEED = 5
BURGER_MAX_SPEED = 2
juice = 100
score = 0

player = Actor('lemon')
player.pos = (WIDTH/2, HEIGHT/2)

pe = ParticleEngine()

def makeBurger():
    global burgers
    burger = Actor('burger')
    burger.pos =(randint(0, WIDTH), randint(0, HEIGHT))
    burger.vx = randint(-BURGER_MAX_SPEED, BURGER_MAX_SPEED)
    burger.vy = randint(-BURGER_MAX_SPEED, BURGER_MAX_SPEED)
    burgers.append(burger)

burgers = []

for n in range(20):
    makeBurger()

def update(dt):
    global juice, score
    
    pe.update(dt)

    if juice > 0:
            
        score += 1
    
        update_player()

        for burger in burgers:

            burger.x  += burger.vx
            burger.y  += burger.vy

            if burger.left < 0 or burger.right > WIDTH:
                burger.vx = -burger.vx

            if burger.top < 0 or burger.bottom > HEIGHT:
                burger.vy = -burger.vy

            if burger.colliderect(player):
                pe.emit((player.x, player.y), config=effects["juice"],emit_duration=-1)
                juice -= 1

    else:
        juice = 0
  

def update_player():

    if keyboard[keys.LEFT]:
        player.left -= PLAYER_SPEED
    elif keyboard[keys.RIGHT]:
        player.left += PLAYER_SPEED

    if keyboard[keys.UP]:
        player.top -= PLAYER_SPEED
    elif keyboard[keys.DOWN]:
        player.top += PLAYER_SPEED

    if player.left < 0:
        player.left = 0
    elif player.right > WIDTH:
        player.right = WIDTH

    if player.top < 0:
        player.top = 0
    elif player.bottom > HEIGHT:
        player.bottom = HEIGHT


def draw():
    screen.clear()
    player.draw()

    for burger in burgers:
        burger.draw()

    screen.draw.text("Lemon Leak", midtop=(WIDTH/2,10), align="Center", fontsize=60, color="Yellow")
    
    screen.draw.text(str(juice),(5,5), fontsize=40, color="Yellow")

    if juice == 0:
        screen.draw.text("Game Over", midtop=(WIDTH/2,100), align="Center", fontsize=160, color="Red" )
        screen.draw.text("Score: {0:0}".format(score), midtop=(WIDTH/2,200), align="Center", fontsize=60, color="Cyan" )

    pe.draw(screen)

pgzrun.go()
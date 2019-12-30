import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

PLAYER_SPEED = 5

countdown = 10
score = 0

player = Actor('alien')
player.pos = (WIDTH/2, HEIGHT/2)

pizza = Actor('pizza')
pizza.pos = (randint(0, WIDTH), randint(0, HEIGHT))

def update(dt):

    global countdown
    countdown -= dt

    if countdown < 0:
        countdown = 0
    else:
        update_player()

def update_player():

    if keyboard[keys.LEFT]:
        player.left -= PLAYER_SPEED
    elif keyboard[keys.RIGHT]:
        player.left += PLAYER_SPEED

    if keyboard[keys.UP]:
        player.top -= PLAYER_SPEED
    elif keyboard[keys.DOWN]:
        player.top += PLAYER_SPEED

    if player.colliderect(pizza):
        eat_pizza()

def draw():
    screen.clear()
    player.draw()
    pizza.draw()

    screen.draw.text("Pizza Hunt", midtop=(WIDTH/2,10), align="Center", fontsize=60, color="Red" )

    screen.draw.text(str(score), (5,5), fontsize=50)
    screen.draw.text('{0:.2f}'.format(countdown), topright=(WIDTH-5, 5), fontsize=50)

    if countdown == 0:
        screen.draw.text("Game Over", midtop=(WIDTH/2,100), align="Center", fontsize=160, color="Orange" )
        screen.draw.text("Score " + str(score), midtop=(WIDTH/2,220), align="Center", fontsize=50, color="Yellow" )
    
def eat_pizza():
    global score
    print("Nom Nom Nom")
    pizza.pos = (randint(0, WIDTH), randint(0, HEIGHT))
    score += 1


pgzrun.go()
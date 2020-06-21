import pgzrun
import pygame
from random import randrange

WIDTH=800
HEIGHT=600

def make_bricks():
    result = []
    w = 10
    h = 8
    x_start = 64 + 16
    y_start = 32
    for y in range(0, h):
        for x in range(0, w):
            brick = Actor('breakout_bricks')
            brick.top = y_start + y * 32
            brick.left = x_start + x * 64
            brick.alive = True
            result.append(brick)

    return result

def reset_ball():
    ball.x = bat.midtop[0]
    ball.y = HEIGHT - 32
    ball.vx = randrange(-20, 20)
    ball.vy = randrange(-20, -5)

def update_ball(dt):
    global lives

    ball.x += dt * ball.vx * 10
    ball.y += dt * ball.vy * 10

    if ball.left < 0:
        ball.left = 0
        ball.vx *= -1

    if ball.right > WIDTH:
        ball.right = WIDTH
        ball.vx *= -1

    if ball.top < 0:
        ball.top = 0
        ball.vy *= -1

    if ball.bottom > HEIGHT:
        reset_ball()
        lives -= 1

def update_bat(dt):

    if keyboard.left:
        bat.x -= dt * bat.speed
    if keyboard.right:
        bat.x += dt * bat.speed

    if bat.left < 0:
        bat.left = 0
    if bat.right > WIDTH:
        bat.right = WIDTH

    if ball.colliderect(bat):
        ball.vy *= -1
        ball.vx += randrange(-5, 5)
        ball.bottom = bat.top -1

def update_bricks(dt):
    global bricks, score

    for brick in bricks:
        if brick.colliderect(ball):
            score += 1
            brick.alive = False
            if brick.collidepoint(ball.midtop) or brick.collidepoint(ball.midbottom):
                ball.vy *= -1 
            elif brick.collidepoint(ball.midleft) or brick.collidepoint(ball.midright):
                ball.vx *= -1

    bricks = [brick for brick in bricks if brick.alive]

def update(dt):
    if lives > 0:
        update_ball(dt)
        update_bat(dt)
        update_bricks(dt)

def draw():
    screen.fill((0, 10, 30))
    screen.draw.text("Lives: {0}".format(lives), (10, 10))
    screen.draw.text("Score: {0}".format(score), (WIDTH - 100, 10))
    
    bat.draw()
    ball.draw()
    for brick in bricks:
        brick.draw()


lives = 3
score = 0

bricks = make_bricks()

bat = Actor("breakout_bat")
bat.top =HEIGHT - 32
bat.left =(WIDTH - bat.width)/2
bat.speed = 250

ball = Actor("breakout_ball")
reset_ball()

pgzrun.go()
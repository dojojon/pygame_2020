import pgzrun
import pygame
from random import randrange

WIDTH=800
HEIGHT=600

def reset_ball():
    ball.x = WIDTH /2
    ball.y = HEIGHT * 0.75
    ball.vx = randrange(-20, 20)
    ball.vy = randrange(-20, -5)

def update_ball(dt):
    global ball

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
        ball.vy *= -1

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

def update(dt):
    update_ball(dt)
    update_bat(dt)
    pass

def draw():
    screen.fill((0, 10, 30))
    screen.draw.text("Lives: {0}".format(lives), (20, 20))
    bat.draw()
    ball.draw()
    pass


lives = 3

ball = Actor("breakout_ball")
reset_ball()

bat = Actor("breakout_bat")
bat.top =HEIGHT - 32
bat.left =(WIDTH - bat.width)/2
bat.speed = 250

pgzrun.go()
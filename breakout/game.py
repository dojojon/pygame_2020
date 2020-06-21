import pgzrun
import pygame
from random import randrange


WIDTH=800
HEIGHT=600

lives = 3

ball = Actor("breakout_ball")
ball.x = 400
ball.y = 400
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


def update(dt):
    update_ball(dt)
    pass

def draw():
    screen.fill((0, 10, 30))
    screen.draw.text("Lives: {0}".format(lives), (20, 20))
    ball.draw()
    pass

pgzrun.go()
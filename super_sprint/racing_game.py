import pgzrun
import math

WIDTH=800
HEIGHT=600

TURN_SPEED = 100
ACCELERATION =  2
BREAK = 3
MAX_SPEED = 2
MAX_REVERSE_SPEED = -.5
DRAG = .5
OFF_TRACK_SPEED = 1.0

TRACK = [
"            h",
" 1hhhhhhh2   ",
" v       v   ",
" v       3h2 ",
" v         v ",
" 3hh2    1h4 ",
"    v    v   ",
"    v    v   ",
"    3hhhh4   ",
"             ",
]

player = Actor("race_car_sm_1", pos=(92, 200), anchor=('center', 'center') )
player.vel = 0

def make_collide_list():
    result = []
    y=0
    for row in TRACK:
        x=0
        for cell in row:
            if cell == " ":
                rect = Rect(x * 64, y * 64, 64, 64)
                result.append(rect)
            x += 1
        y += 1

    return result

collide_rects = make_collide_list()

def update_player(dt):

    if keyboard.up or keyboard.a:
        player.vel += ACCELERATION * dt
    elif keyboard.down or keyboard.z:
        player.vel -= BREAK * dt
    elif player.vel > 0:
        player.vel -= DRAG * dt

    if keyboard.left:
        player.angle += TURN_SPEED * dt

    if keyboard.right:
        player.angle -= TURN_SPEED * dt

    if player.vel > MAX_SPEED:
        player.vel = MAX_SPEED
    elif player.vel < MAX_REVERSE_SPEED:
        player.vel = MAX_REVERSE_SPEED

    angle_radians = math.radians(player.angle)
    pos_x = math.sin(angle_radians) * -player.vel
    pos_y = math.cos(angle_radians) * -player.vel
    player.center = (player.center[0] + pos_x ,player.center[1] + pos_y)

    for rect in collide_rects:
        if player.colliderect(rect):
            if player.vel > OFF_TRACK_SPEED:
                player.vel = OFF_TRACK_SPEED

    if player.left < 0 or player.right > WIDTH:
        player.vel = player.vel * -.1
    if player.top < 0 or player.bottom > HEIGHT:
        player.vel =  player.vel * -.1

def update(dt):
    update_player(dt)


def draw_track():

    y = 0
    for row in TRACK:
        x = 0
        for cell in row:

            if cell == "v":
                screen.blit("road1v", (x,y))
            elif cell == "h":
                screen.blit("road1h", (x,y))
            elif cell == "1":
                screen.blit("road1tl", (x,y))
            elif cell == "2":
                screen.blit("road1tr", (x,y))
            elif cell == "3":
                screen.blit("road1bl", (x,y))
            elif cell == "4":
                screen.blit("road1br", (x,y))
            x += 64
        y += 64

def draw_collision_map():

    for rect in collide_rects:
        screen.draw.rect(rect, (200,200,0))

def draw():

    screen.fill((30, 200, 40))

    draw_track()
    draw_collision_map();
    player.draw()

pgzrun.go()
import pgzrun
import math
from common.particle_engine import ParticleEngine, effects

WIDTH=800
HEIGHT=640

GRAVITY=25
ROTATE_RATE = 150
THRUST = -100

game_over = False
good_landing = False

pe = ParticleEngine()

MAP = [

"0000000000000000000000000",
"0000000000000000000000000",
"0000000000000000000000000",
"0000001000000000000000000",
"0000001000000000000000011",

"0000001100000000000000000",
"0000011100000000000111111",
"1111111110000000111111111",
"1111111111000000000111111",
"1111111100000000000000111",

"0000000000000000000000011",
"0000000000000000000111111",
"0000000000000000000000111",
"0000000000000000000000011",
"0000000000100000000000000",

"0000000001100000000000000",
"0000000011110000000000010",
"1111111111111000000000111",
"1111111111111112222111111",
"1111111111111111111111111",
]

player = Actor('lander')
player.x = 32
player.y = 32
player.vy= 0
player.vx= 0

# player.x = WIDTH/2
# player.y = HEIGHT/2
# GRAVITY =0

def update(dt):

    pe.update(dt)

    if not game_over:
        update_player(dt)
        check_player_map()

def check_player_map():
    global game_over, good_landing

    landing_pad = get_map_rects_around_point(player.center, cell_type="2")
    for rect in landing_pad:
        if player.colliderect(rect):
            game_over = True
            if player.angle > 350 or player.angle < 10:
                good_landing = True
            else:
                explode_ship()

    hit_rects = get_map_rects_around_point(player.center, cell_type="1")
    for rect in hit_rects:
        if player.colliderect(rect):
            game_over = True
            explode_ship()

def explode_ship():
    pe.emit(player.center, config=effects["shockWave"], volume=9, emit_duration=1)

def update_player(dt):
    player.vy  += GRAVITY * dt
    player.y += player.vy * dt
    player.x += player.vx * dt

    if keyboard.a:
        player.angle += dt * ROTATE_RATE

    if keyboard.d:
        player.angle  -= dt * ROTATE_RATE

    if player.angle < 0:
        player.angle = 360 + player.angle

    if player.angle > 360:
        player.angle = player.angle - 360

    if keyboard.space:
        rotate_rads = math.radians(player.angle)
        player.vy += dt * THRUST * math.cos(rotate_rads)
        player.vx += dt * THRUST * math.sin(rotate_rads)

    if keyboard.s:
        player.vx = 0
        player.vy = 0


def draw():

    screen.fill((0,0,0))
    
    player.draw()

    draw_map()

    screen.draw.text("{}".format(player.angle), center=(20 + WIDTH/2 , -20 +HEIGHT/2), color=(255,0,0), fontsize=20 )

    if game_over:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), color=(255,0,0), fontsize=180 )
   
    if good_landing:
        screen.draw.text("Good Landing", center=(WIDTH/2, 60 + HEIGHT/2), color=(0,255,0), fontsize=120 )


    pe.draw(screen)

def get_map_rects_around_point(point, cell_type=None):

    rects = []
    map_x = int((point[0] +16) /32)
    map_y = int((point[1] +16)/32)

    map_x_min = map_x -1
    if map_x_min < 0:
        map_x_min = 0
    map_x_max = map_x + 1
    if map_x_max > WIDTH /32:
        map_x_max = int(WIDTH/32)
    
    map_y_min = map_y -1
    if map_y_min < 0:
        map_y_min = 0
   
    map_y_max = map_y + 1
    if map_y_max > HEIGHT /32:
        map_y_max = int(HEIGHT/32)

    for y in range(map_y_min, map_y_max):
        for x in range(map_x_min, map_x_max):

            map_cell = MAP[y][x]
            if cell_type == None or cell_type == map_cell:
                rect = Rect(x * 32, y * 32, 32, 32)
                rects.append(rect)

    return rects


def draw_map():

    y=0
    for row in MAP:
        
        x=0
        for cell in row:

            if cell == "1":
                r = Rect(x, y, 32, 32)
                screen.draw.filled_rect(r, (99,79,53))
            elif cell == "2":
                r = Rect(x, y, 32, 32)
                screen.draw.filled_rect(r, (200,40,53))

            x+=32
        y+=32


pgzrun.go()

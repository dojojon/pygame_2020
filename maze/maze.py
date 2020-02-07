import pgzrun


WIDTH = 640
HEIGHT = 480
CELL_SIZE = 32

MAP = [

"wwwwwwwwwwwwwwwwwwww",
"w000000000000000000w",
"w00wwwwwwwwwwwww000w",
"w00w0000s0w0k00w000w",
"w00w000000w0000w000w",

"w000000000w00000000w",
"w000000000w00000000w",
"wdwwwwwwwwwwwwwwwwww",
"w000000000000000000w",
"w000000000000000000w",

"w000000000000000000w",
"wwwwww000000000wwdww",
"w0000wwwww00000w000w",
"w00000000000000w000e",
"wwwwwwwwwwwwwwwwwwww",

]
game_over = False

def get_player_start():

    result = (0, 0)
    y = 0
    x = 0
    for row in MAP:
        x += 1
        for cell in row:
            if cell == "s":
                result = (x, y)

        y += 1
    return result


start = get_player_start()

player = Actor("fred")
player.position = start
player.next_move_time = 0

def update(dt):
    global game_over

    if not game_over:
        update_player(dt)
    
    if get_cell_type (player.position) == "e":
        game_over = True


def update_player(dt):

    player.next_move_time -= dt

    if player.next_move_time < 0:

        if keyboard.right and can_walk((1, 0)):
            player.position = (player.position[0] + 1, player.position[1])
            player.next_move_time = 0.125

        if keyboard.left and can_walk((-1, 0)):
            player.position = (player.position[0] - 1, player.position[1])
            player.next_move_time = 0.125

        if keyboard.up and can_walk((0, -1)):
            player.position = (player.position[0] ,  player.position[1] -1 )
            player.next_move_time = 0.125

        if keyboard.down and can_walk((0, 1)):
            player.position = (player.position[0] ,  player.position[1] + 1)
            player.next_move_time = 0.125
        
    print("player {}".format(player.position))
    player.topleft = (player.position[0]* CELL_SIZE, player.position[1]* CELL_SIZE)


def can_walk(direction):
    no_walk = ["w"]
    player_check_position = (player.position[0] + direction[0], player.position[1] + direction[1])
    cell = get_cell_type(player_check_position)
    return  cell not in no_walk


def get_cell_type(position):
    row = MAP[position[1]]
    cell = row[position[0]]
    return cell
    

def draw():
    screen.fill((50,50,50))
    draw_map()
    player.draw()

    if game_over:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), color=(255,0,255), fontsize=100 )




def draw_map():

    tiles = {
        "w": "wall",
        "d": "door",
        "k":  "key",
        # "e": (255, 100, 100)
    }

    y=0
    for row in MAP:
        
        x=0
        for cell in row:

            image = tiles.get(cell)
            if image is not None:
                r = Rect(x, y, CELL_SIZE, CELL_SIZE)
                # screen.draw.filled_rect(r, color)
                screen.blit(image, (x,y))

            x+=CELL_SIZE

        y+=CELL_SIZE

pgzrun.go()

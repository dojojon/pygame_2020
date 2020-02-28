import pgzrun


WIDTH = 640
HEIGHT = 480
CELL_SIZE = 32

MAP = [

"wwwwwwwwwwwwwwwwwwww",
"w000000000000000000w",
"w00wwwwwwwwwwwww000w",
"w00w0000s0w0k00w000w",
"w00w000000w00m0w000w",

"w000000000w00000000w",
"w000000000w00000000w",
"wdwwwwwwwwwwwwwwwwww",
"w000000000w00000000w",
"w000000000w0000m000w",

"w000w0m000w0m00w000w",
"wwwwwww0000000wwwdww",
"wk0000wwww0000w0000w",
"w000000m00000w00000e",
"wwwwwwwwwwwwwwwwwwww",

]
game_over = False

def get_monsters():


    result = []
    y = 0
    for row in MAP:
        x = 0
        for cell in row:
            if cell == "m":
                monster = Actor('skelly')
                monster.position = (x,y)
                monster.direction = (1, 0)
                monster.next_move_interval = .25
                monster.next_move_time  = .25
                result.append(monster)
            x += 1

        y += 1
    return result


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
player.keys = 0

monsters = get_monsters()

def update(dt):
    global game_over

    for monster in monsters:
        monster.next_move_time -= dt
        if monster.next_move_time < 0:
            monster.next_move_time = monster.next_move_interval

            if not can_walk(monster.position, monster.direction):
                monster.direction = (monster.direction[0] * -1, monster.direction[1] * -1)

            monster.position = (monster.position[0] + monster.direction[0], monster.position[1] + monster.direction[1])

        monster.topleft = (monster.position[0] * CELL_SIZE, monster.position[1] * CELL_SIZE)

        if monster.colliderect(player):
            game_over = True
            player.image = "skelly"
            

    if not game_over:
        update_player(dt)
    
    if get_cell_type (player.position) == "e":
        game_over = True

    cell = get_cell_type(player.position)
    if cell == "k":
        set_cell_type(player.position,0)
        player.keys += 1

def update_player(dt):

    player.next_move_time -= dt

    if player.next_move_time < 0:

        if keyboard.right and can_walk(player.position, (1, 0)):
            player.position = (player.position[0] + 1, player.position[1])
            player.next_move_time = 0.125

        if keyboard.left and can_walk(player.position, (-1, 0)):
            player.position = (player.position[0] - 1, player.position[1])
            player.next_move_time = 0.125

        if keyboard.up and can_walk(player.position, (0, -1)):
            player.position = (player.position[0] ,  player.position[1] -1 )
            player.next_move_time = 0.125

        if keyboard.down and can_walk(player.position, (0, 1)):
            player.position = (player.position[0] ,  player.position[1] + 1)
            player.next_move_time = 0.125
        
    print("player keys {}".format(player.keys))
    player.topleft = (player.position[0]* CELL_SIZE, player.position[1]* CELL_SIZE)


def can_walk(position, direction):
    no_walk = ["w", "d"]
    check_position = (position[0] + direction[0], position[1] + direction[1])
    cell = get_cell_type(check_position)

    if cell == "d" and player.keys > 0:
        set_cell_type(check_position, "0")
        player.keys -= 1
        cell = get_cell_type(check_position)

    return  cell not in no_walk


def get_cell_type(position):
    row = MAP[position[1]]
    cell = row[position[0]]
    return cell

def set_cell_type(position, cell_type):
    global MAP
    row = MAP[position[1]]
    cells = list(row)
    cells[position[0]] = str(cell_type)
    MAP[position[1]] = ''.join(cells)

def draw():
    screen.fill((50,50,50))
    draw_map()
    player.draw()

    for monster in monsters:
        monster.draw()

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

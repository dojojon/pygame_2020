from random import randint

WIDTH=800
HEIGHT=640

player=Actor("wizards/fred")
player.left = WIDTH/2
player.top = 200
game_over = False

baddies = []

for n in range(0, 10):
    virus = Actor("wizards/virus")
    virus.left = randint(60, WIDTH -60)
    virus.top = randint(60, HEIGHT -60)

    virus.vx = randint(-300, 300)
    virus.vy = randint(-300, 300)

    baddies.append(virus)

def update_player(dt):

    if keyboard.left:
        player.left -=200 * dt
    elif keyboard.right:
        player.left +=200 * dt

    if keyboard.up:
        player.top -=200 * dt
    elif keyboard.down:
        player.top +=200 * dt

def update_virus(dt):

    for virus in baddies:
        virus.left += virus.vx * dt
        virus.top += virus.vy * dt

        if virus.left < 0:
            virus.vx *= -1

        if virus.right > WIDTH:
            virus.vx *= -1

        if virus.top < 0:
            virus.vy *= -1

        if virus.bottom > HEIGHT:
            virus.vy *= -1

def check_player():
    global game_over
    for virus in baddies:
        if virus.colliderect(player):
            game_over = True

def display_game_over():

    if game_over:
        screen.draw.text("Game Over",center=(WIDTH/2, HEIGHT/2),fontsize=200,  color=(255,100,20))

def update(dt):

    update_virus(dt)

    update_player(dt)

    check_player()

def draw():
    screen.fill((255, 0, 240))
    player.draw()

    for virus in baddies:
        virus.draw()

    display_game_over()

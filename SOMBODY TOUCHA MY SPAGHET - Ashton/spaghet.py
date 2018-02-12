# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

#Images
spaghet = pygame.image.load('Spaghet.png')
noodle = pygame.image.load('noodle.png')
sauce = pygame.image.load('sky.png')
noodles = pygame.image.load('grass.png')
meatball = pygame.image.load('sun.png')
somebody = pygame.image.load('somebody.png')
fsm = pygame.image.load('fsm.png')

# Window
SIZE = (800, 600)
TITLE = "Spaghet"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)

# Gravity
gforce = 5

# Sound Effects
pygame.mixer.music.load("sounds/music.ogg")
stms = pygame.mixer.Sound("sounds/stms.ogg")

# Make clouds
stormy = True

num_clouds = 30
near_clouds = []
for i in range(num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 200)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(spaghet, (x, y))

# Make rain
num_rain = 20
rain = []
for i in range(num_rain):
    x = random.randrange(0, 1000)
    y = random.randrange(-600, 0)
    loc = [x, y]
    rain.append(loc)

def draw_rain(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(noodle, (x,y))

lightning_timer = 0

# Spaghetti Monster
fx = 0
fy = 400
xspeed = 0
yspeed = 0
flightcount = 120
   
# Game loop
pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xspeed -= 5
            elif event.key == pygame.K_RIGHT:
                xspeed += 5
            elif event.key == pygame.K_UP:
                yspeed -= 10
                flightcount -= 2
            elif event.key == pygame.K_DOWN:
                yspeed += 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xspeed = 0
            elif event.key == pygame.K_RIGHT:
                xspeed = 0
            elif event.key == pygame.K_UP:
                yspeed = 0
                flightcount += 1
            elif event.key == pygame.K_DOWN:
                yspeed = 0
        elif event.type == pygame.QUIT:
            done = True

    # Game logic
    fx += xspeed
    fy += yspeed

    if flightcount == 0:
        yspeed == 0
    elif flightcount > 60:
        flightcount -= 1

    if fy > 420:
        pass
    else:
        fy += gforce

    if fx < -10:
        fx += 5
    elif fx > 635:
        fx -= 5

    if fy > 420:
        fy -= 5
    elif fy < 0:
        fy += 5
    
    for c in near_clouds:
        c[0] += 2

        if c[0] < -200:
           c[0] = random.randrange(-800, -100)
           c[1] = random.randrange(-50, 200)

    for c in far_clouds:
        c[0] -= 1

        if c[0] < -200:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)
            

    for r in rain:
        r[0] -= 2
        r[1] += 9

        if r[1] > 400 or r[0] < -50:
            r[1] = random.randrange(-600, 0)
            r[0] = random.randrange(-10, 900)

    ''' flash lighting '''
    if stormy:
        if random.randrange(0, 150) == 0:
            stms.play()
            lightning_timer = 20
        else:
            lightning_timer -= 1
             
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.blit(somebody, (0, 0))
    else:
        screen.blit(sauce, (0, 0))

    ''' sun '''
    screen.blit(meatball, (575, 25))

    ''' far clouds '''
    for c in far_clouds:
        draw_cloud(c)

    ''' grass '''
    screen.blit(noodles, (0, 400))


    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' rain '''
    for r in rain:
        draw_rain(r)

    ''' near clouds '''
    for c in near_clouds:
        draw_cloud

    ''' Spaghetti Monster '''
    screen.blit(fsm, (fx, fy))


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

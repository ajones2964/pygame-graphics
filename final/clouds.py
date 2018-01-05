# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Midnight Spaghet"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 96, 11)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GRAY = (50, 50, 50)
BLACK = (0, 0, 0)
BROWN = (165, 55, 0)

# Images
spaghet = pygame.image.load('Spaghet.png')

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GRAY, [x + 20, y + 20, 60, 40])

stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0,400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)

   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic

             
    # Drawing code
    ''' sky '''
    screen.fill(BLACK)

    ''' stars '''
    for s in stars:
        pygame.draw.ellipse(screen, YELLOW, s)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' table '''
    pygame.draw.rect(screen, BROWN, [200, 350, 10, 350])
    pygame.draw.rect(screen, BROWN, [250, 350, 10, 350])
    pygame.draw.rect(screen, BROWN, [190, 350, 80, 10])

    ''' images '''
    screen.blit(spaghet, (155, 280))

    ''' clouds '''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    

    #pygame.draw.rect(screen, 


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

import pygame
import time

# config
window_witdh, window_height = 600,600
initial_pos_x, initial_pos_y = 100, 100

pygame.init()
screen = pygame.display.set_mode((window_witdh, window_height))
clock = pygame.time.Clock()

vamp = pygame.image.load(r'resources\pix\bat_xs.png').convert_alpha()
x, y = initial_pos_x/2, initial_pos_y/2
velocity = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0,0,0))
    # movement with arrow keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= velocity
        velocity += 1
        still_pressing = True
    else:
        still_pressing = False
    if pressed[pygame.K_DOWN]:
        y += velocity
        velocity += 1
        still_pressing = True
    if pressed[pygame.K_RIGHT]:
        x += velocity
        velocity += 1
        still_pressing = True
    if pressed[pygame.K_LEFT]:
        x -= velocity
        velocity += 1
        still_pressing = True
    
    if still_pressing == False:
        velocity=1
    screen.blit(vamp,(x,y))

    if x < 0:
        x = window_witdh
    elif x > window_witdh:
        x = 0
    if y < 0:
        y = window_height
    elif y > window_height:
        y = 0

    pygame.display.update()
    clock.tick(30)
    
import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_w, K_s, KEYDOWN, KEYUP

pygame.init()

FPS = pygame.time.Clock()

# Initials
HEIGHT = 600
WIDTH = 1000

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
bg = pygame.transform.scale(pygame.image.load('./PyGame_Pong/src/background_2.jpg'), (WIDTH, HEIGHT))

playing = True

angle = [(1.4, 0.7), (0.7, 0.7), (0.7, 1.4)]

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = 'darkcyan'

# Fonts
FONT = pygame.font.SysFont("Verdana", 32)

# Ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius  # center of display
ball_vel_x, ball_vel_y = 1, 1

# Pads
pad_width, pad_height = 20, 120
left_pad_y = right_pad_y = HEIGHT/2 - pad_height/2
left_pad_x = 50 - pad_width/2
right_pad_x = WIDTH - (50 + pad_width/2)
right_pad_speed = left_pad_speed = 0
right_pad_score = left_pad_score = 0

# Game loop
while playing:
    FPS.tick(240)
    main_display.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                right_pad_speed = 1
            if event.key == K_UP:
                right_pad_speed = -1
            if event.key == K_s:
                left_pad_speed = 1
            if event.key == K_w:
                left_pad_speed = -1

        if event.type == KEYUP:
            right_pad_speed = 0
            left_pad_speed = 0

    # Ball's movement
    if ball_y < 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x < 0 + radius:                                   # end round, left player win
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius  # return ball to center of display
        random_ang = random.choice(angle)                     # random start speed and angle of the ball's reflection
        ball_vel_x, ball_vel_y = random_ang
        ball_vel_y *= random.choice([1, -1])
        ball_vel_x *= -1
        left_pad_score += 1                                   # set score point

    if ball_x > WIDTH - radius:                               # end round, right player win
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius  # return ball to center of display
        ang = random.choice(angle)                            # random start speed and angle of the ball's reflection
        random_ang = random.choice(angle)
        ball_vel_x, ball_vel_y = random_ang
        ball_vel_y *= random.choice([1, -1])
        right_pad_score += 1                                  # set score point

    # Pad's movement
    if right_pad_y <= 0:
         right_pad_y = 0
    if right_pad_y >= HEIGHT - pad_height:
         right_pad_y = HEIGHT - pad_height
    if left_pad_y <= 0:
         left_pad_y = 0
    if left_pad_y >= HEIGHT - pad_height:
         left_pad_y = HEIGHT - pad_height

    # Collisions
    #left pad
    if (
        left_pad_x <= ball_x <= left_pad_x + pad_width 
        and left_pad_y <= ball_y <= left_pad_y + pad_height 
        ):
        ball_x = left_pad_x + pad_width
        ball_vel_x *= -1
        
    #right pad
    if (
        right_pad_x <= ball_x <= right_pad_x + pad_width
        and right_pad_y <= ball_y <=  right_pad_y + pad_height
        ):
        ball_x = right_pad_x
        ball_vel_x *= -1

    # Movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_pad_y += right_pad_speed
    left_pad_y += left_pad_speed

    # Scoreboard
    main_display.blit(FONT.render(f'{left_pad_score} : {right_pad_score}', True, WHITE), (WIDTH/2 - 38, 25))


    # Creating objects
    pygame.draw.circle(main_display, WHITE, (ball_x, ball_y), radius)
    pygame.draw.rect(main_display, RED, pygame.Rect(left_pad_x, left_pad_y, pad_width, pad_height))
    pygame.draw.rect(main_display, RED, pygame.Rect(right_pad_x, right_pad_y, pad_width, pad_height))
    pygame.display.update()

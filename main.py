import pygame
import random
pygame.init()

White = (255, 255, 255)

screen = pygame.display.set_mode((800, 600), pygame.HWSURFACE)

lose = pygame.image.load("lose.png")
lose = pygame.transform.scale(lose, (350, 175))

win = pygame.image.load("win.jpg")
win = pygame.transform.scale(win, (220, 220))

wall = pygame.image.load("line.png")
wall = pygame.transform.scale(wall, (300, 900))

angle = [-60, -40, -20, 20, 40, 60]
ball_angle = 0
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ball_x = 375
ball_y = 275
x_vel = 3
y_vel = 0

line1 = pygame.image.load("line.png")
line1 = pygame.transform.scale(line1, (500, 120))

line1_y = 275
up1 = False
down1 = False
line2 = pygame.image.load("line.png")
line2 = pygame.transform.scale(line2, (500, 120))

line2_y = 275
up2 = False
down2 = False

run = True
clock = pygame.time.Clock()
FPS = 60
x_vel_vel = 0.001
while run:
    clock.tick(FPS)
    screen.fill(White)
    screen.blit(wall, (250, -100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up2 = True
            if event.key == pygame.K_DOWN:
                down2 = True
            if event.key == pygame.K_w:
                up1 = True
            if event.key == pygame.K_s:
                down1 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up2 = False
            if event.key == pygame.K_DOWN:
                down2 = False
            if event.key == pygame.K_w:
                up1 = False
            if event.key == pygame.K_s:
                down1 = False
    if up1:
        line1_y -= 3
    if down1:
        line1_y += 3
    if up2:
        line2_y -= 3
    if down2:
        line2_y += 3
    ball_x += x_vel
    ball_y += y_vel
    if ball_x >= 700 and line2_y + 110 >= ball_y >= line2_y - 25:
        x_vel = -x_vel
        ball_angle = random.choice(angle)
        x_vel_vel = -x_vel_vel
    if ball_x <= 50 and line1_y + 110 >= ball_y >= line1_y - 25:
        x_vel = -x_vel
        ball_angle = random.choice(angle)
        x_vel_vel = -x_vel_vel
    if ball_angle == -60:
        y_vel -= 0.01
    if ball_angle == -40:
        y_vel -= 0.007
    if ball_angle == -20:
        y_vel -= 0.0035
    if ball_angle == 60:
        y_vel == 0.01
    if ball_angle == 40:
        y_vel += 0.007
    if ball_angle == 20:
        y_vel += 0.0035
    if ball_y <= 0:
        y_vel = -y_vel
    if ball_y >= 550:
        y_vel = -y_vel
    x_vel += x_vel_vel
    if ball_x >= 800:
        first_lose = True
        over = True
        run = False
    if ball_x <= -50:
        first_lose = False
        over = True
        run = False
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(line1, (-200, line1_y))
    screen.blit(line2, (500, line2_y))
    pygame.display.update()
while over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
    if first_lose:
        screen.blit(lose, (400, 200))
        screen.blit(win, (100, 150))
    else:
        screen.blit(lose, (40, 200))
        screen.blit(win, (440, 150))
    pygame.display.update()

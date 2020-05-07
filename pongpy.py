import pygame
import sys
import random

def ballScript():
    global ball_speed_x
    global ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if ball.left <= 0 or ball.right >= screen_width:   
        restart()
    
    if ball.colliderect(player)  or ball.colliderect(robot):
        ball_speed_x *= -1


def restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


def player():

    player.y += velocity

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def robot():
    robot.y += rvelocity

    if robot.top <= 0:
        robot.top = 0
    if robot.bottom >= screen_height:
        robot.bottom = screen_height


    

pygame.init()
colock = pygame.time.Clock()


screen_width =1000
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('PongPy @Cryp70n1c-W45p ')


# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

ball_speed_x = 8 * random.choice((1,-1))
ball_speed_y = 8 * random.choice((1,-1))
velocity = 0
rvelocity = 0
# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
robot = pygame.Rect(10, screen_height / 2 - 70, 10,140)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocity +=8
            if event.key == pygame.K_UP:
                velocity -=8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                velocity -=8
            if event.key == pygame.K_UP:
                velocity +=8   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                rvelocity +=8
            if event.key == pygame.K_w:
                rvelocity -=8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                rvelocity -=8
            if event.key == pygame.K_w:
                rvelocity +=8   
    
    
    ballScript()
    player()
    robot()
    
    player.y +=velocity
    robot.y += rvelocity
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,robot)
    pygame.draw.ellipse(screen,light_grey,ball)

    pygame.display.flip()
    colock.tick(60)
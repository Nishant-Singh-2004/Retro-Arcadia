import pygame
import random
pygame.init()
from os.path import join

#imports
font =pygame.font.Font(join("Oxanium-Bold.ttf"),30)
winning_font=pygame.font.Font(join("Oxanium-Bold.ttf"),90)
#intials
width,height =1000,600
wn = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ping Pong -(suraj pandey)")
run =True
direction = [0, 1]
angle = [0, 1, 2]
player_1=player_2=0
#colors
BLUE = 'aqua'
RED ='chartreuse3'
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
#ball
radius = 15
ball_x,ball_y= width/2-radius,height/2-radius
ball_vel_x , ball_vel_y =0.3,0.3

#balls movements control

if ball_y<=0+radius or ball_y>=height-radius:
    ball_vel_y*=-1

#paddles_dimensions
paddle_width,paddle_height = 20,120
left_paddle_y =right_paddle_y = height/2-paddle_height/2
left_paddle_x , right_paddle_x = 100-paddle_width/2,width-(100-paddle_width/2)
#paddle movement
right_paddle_vel = left_paddle_vel = 0


#main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
           run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.7
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.7
            if i.key == pygame.K_w:
                left_paddle_vel = -0.7
            if i.key == pygame.K_s:
                left_paddle_vel = 0.7
        elif i.type==pygame.KEYUP:
            left_paddle_vel=0
            right_paddle_vel=0

    #collision with paddles\
    if left_paddle_x<=ball_x<=left_paddle_x+paddle_width:
        if left_paddle_y<=ball_y<=left_paddle_y+paddle_height:
            ball_x=left_paddle_x+paddle_width
            ball_vel_x*=-1
    if right_paddle_x<=ball_x<=right_paddle_x+paddle_width:
        if right_paddle_y<=ball_y<=right_paddle_y+paddle_height:
            ball_x= right_paddle_x
            ball_vel_x*=-1

    #paddles movements controls
    if right_paddle_y>=height-paddle_height:
        right_paddle_y=height-paddle_height
    if right_paddle_y<=0:
        right_paddle_y=0
    if left_paddle_y>=height-paddle_height:
        left_paddle_y=height-paddle_height
    if left_paddle_y<=0:
        left_paddle_y=0
    #balls movements control
    if ball_y<=0+radius or ball_y>=height-radius:
        ball_vel_y*=-1
    if ball_x>=width-radius:
        player_1+=1
        ball_x,ball_y = width/2-radius,height/2-radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.4, 0.5
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.4, 0.3
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.4, 0.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.4, 0.5
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.3, 0.4
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.4, 0.4
        ball_vel_x *= -1
    if ball_x<=0+radius:
        player_2+=1
        ball_x,ball_y = width/2-radius,height/2-radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.4, 0.3
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.4, 0.3
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.4, 0.4
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.4, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.3, 0.4
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.4, 0.4
        ball_vel_x *= -1      
    

    #movement
    ball_x+=ball_vel_x
    ball_y+= ball_vel_y  
    left_paddle_y+=left_paddle_vel
    right_paddle_y+=right_paddle_vel
    #scoreboard
    score_1 =font.render("Player_1:" + str(player_1), True, WHITE)
    wn.blit(score_1,(25, 25))
    score_2 = font.render("Player_2:" + str(player_2), True, WHITE)
    wn.blit(score_2, (825, 25))  
    #objects
    pygame.draw.circle(wn,BLUE,(ball_x,ball_y),radius)
    pygame.draw.rect(wn,RED,pygame.Rect(left_paddle_x,left_paddle_y,paddle_width,paddle_height))
    pygame.draw.rect(wn,RED,pygame.Rect(right_paddle_x,right_paddle_y,paddle_width,paddle_height))

    #endscreen
    if player_1 >= 5:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER_1 WON!!!!", True, WHITE)
        wn.blit(endscreen, (150, 250))
    
    if player_2 >= 5:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER_2 WON!!!!", True, WHITE)
        wn.blit(endscreen, (150, 250))

    pygame.display.update()


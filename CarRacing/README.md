import pygame   #import pygame library
pygame.init()

import random  #importing random
import time  #import time module

width=800
height=600
green = (0,100,0)
green2 = (0,255,0)
red = (100,0,0)
red2 = (255,0,0)
blue = (0,0,100)
blue2 = (0,0,255)

screen = pygame.display.set_mode((width,height))  #screen size

pygame.display.set_caption("RACING GAME")  #caption

clock = pygame.time.Clock()  #managing the frame rate


carimg = pygame.image.load("car1.jpg")  #loading images
grass = pygame.image.load("grass.jpg")
yellow_strip = pygame.image.load("yellow_strip.jpg")
strip = pygame.image.load("strip.jpg")
intro_image = pygame.image.load("intro.jpg")
instruction_background = pygame.image.load("background.jpg")
instruction_background2 = pygame.image.load("background2.jpg")

myfont = pygame.font.SysFont("None",100)  #adding crashed message
render_text = myfont.render("CAR CRASHED",1,(0,0,0))

def intro_loop():  #introduction page
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(intro_image,(0,0))
        
        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if mouse[0] > 60 and mouse[0] < 210 and mouse[1] > 537 and mouse[1] <587:  #start button
            pygame.draw.rect(screen,green2,(60,537,150,50))
            if click == (1,0,0):
                countdown()
        else:
            pygame.draw.rect(screen,green,(60,537,150,50))

        small_text = pygame.font.Font("freesansbold.ttf",20)
        text_surface,text_rect = text_object("START",small_text)
        text_rect.center = ((60+(150/2)),(537+(50/2)))
        screen.blit(text_surface,text_rect)

        if mouse[0] > 310 and mouse[0] < 490 and mouse[1] > 537 and mouse[1] <587:  #instruction button
            pygame.draw.rect(screen,blue2,(310,537,180,50))
            if click == (1,0,0):
                instruction()
        else:
            pygame.draw.rect(screen,blue,(310,537,180,50))
        
        text_surface,text_rect = text_object("INSTRUCTIONS",small_text)
        text_rect.center = ((310+(180/2)),(537+(50/2)))
        screen.blit(text_surface,text_rect)

        if mouse[0] > 590 and mouse[0] < 740 and mouse[1] > 537 and mouse[1] <587:  #quit button
            pygame.draw.rect(screen,red2,(590,537,150,50))
            if click == (1,0,0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen,red,(590,537,150,50))

        text_surface,text_rect = text_object("QUIT",small_text)
        text_rect.center = ((590+(150/2)),(537+(50/2)))
        screen.blit(text_surface,text_rect)

        pygame.display.update()

def pause_page(): #defining pause page
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruction_background2,(0,0))

        large_text = pygame.font.Font("freesansbold.ttf",115)
        text_surface,text_rect = text_object("PAUSED",large_text)
        text_rect.center = (400,300)
        screen.blit(text_surface,text_rect)

        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if mouse[0] > 70 and mouse[0] < 220 and mouse[1] > 450 and mouse[1] <500:  #continue button
            pygame.draw.rect(screen,green2,(70,450,150,50))
            if click == (1,0,0):
                pause = False
                countdown()
        else:
            pygame.draw.rect(screen,green,(70,450,150,50))
  
        small_text = pygame.font.Font("freesansbold.ttf",20)
        text_surface,text_rect = text_object("CONTINUE",small_text)
        text_rect.center = ((70+(150/2)),(450+(50/2)))
        screen.blit(text_surface,text_rect)

        if mouse[0] > 325 and mouse[0] < 475 and mouse[1] > 450 and mouse[1] <500:  #restart button
            pygame.draw.rect(screen,red2,(325,450,150,50))
            if click == (1,0,0):
                countdown()
        else:
            pygame.draw.rect(screen,red,(325,450,150,50))

        small_text = pygame.font.Font("freesansbold.ttf",20)
        text_surface,text_rect = text_object("RESTART",small_text)
        text_rect.center = ((325+(150/2)),(450+(50/2)))
        screen.blit(text_surface,text_rect)

        if mouse[0] > 580 and mouse[0] < 730 and mouse[1] > 450 and mouse[1] <500:  #main menu button
            pygame.draw.rect(screen,blue2,(580,450,150,50))
            if click == (1,0,0):
                intro_loop()
        else:
            pygame.draw.rect(screen,blue,(580,450,150,50))

        small_text = pygame.font.Font("freesansbold.ttf",20)
        text_surface,text_rect = text_object("MAIN MENU",small_text)
        text_rect.center = ((580+(150/2)),(450+(50/2)))
        screen.blit(text_surface,text_rect)

        pygame.display.update()
        clock.tick(30)

def instruction():
    instruction = True
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        screen.blit(instruction_background,(0,0))

        pygame.draw.rect(screen,red,(10,380,310,190))

        large_text = pygame.font.Font("freesansbold.ttf",80)
        medium_text = pygame.font.Font("freesansbold.ttf",40)
        small_text = pygame.font.Font("freesansbold.ttf",20)

        text_surface1,text_rect1 = text_object("90's Car Game",medium_text)
        text_rect1.center = ((400,180))
        screen.blit(text_surface1,text_rect1)

        text_surface2,text_rect2 = text_object("INSTRUCTION",large_text)
        text_rect2.center = ((400,90))
        screen.blit(text_surface2,text_rect2)

        text_surface3,text_rect3 = text_object("ARROW LEFT : LEFT TURN",small_text)
        text_rect3.center = ((165,400))
        screen.blit(text_surface3,text_rect3)

        text_surface4,text_rect4 = text_object("ARROW RIGHT : RIGHT TURN",small_text)
        text_rect4.center = ((165,450))
        screen.blit(text_surface4,text_rect4)

        text_surface6,text_rect6 = text_object("S : ACCELERATOR",small_text)
        text_rect6.center = ((165,500))
        screen.blit(text_surface6,text_rect6)

        text_surface7,text_rect7 = text_object("B : BRAKE",small_text)
        text_rect7.center = ((165,550))
        screen.blit(text_surface7,text_rect7)

        text_surface8,text_rect8 = text_object("CONTROLS",medium_text)
        text_rect8.center = ((400,250))
        screen.blit(text_surface8,text_rect8)

        pygame.draw.rect(screen,green,(580,500,150,50))

        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if mouse[0] > 580 and mouse[0] < 730 and mouse[1] > 500 and mouse[1] <550:  #colour of the buttons
            pygame.draw.rect(screen,green2,(580,500,150,50))
            if click == (1,0,0):
                intro_loop()
        else:
            pygame.draw.rect(screen,green,(580,500,150,50))
        small_text = pygame.font.Font("freesansbold.ttf",30)
        text_surface,text_rect = text_object("BACK",small_text)
        text_rect.center = ((580+(150/2)),(500+(50/2)))
        screen.blit(text_surface,text_rect)

        pygame.display.update()
        clock.tick(30)

def text_object(text,font):
    text_surface = font.render(text, True, (0,0,0))
    return text_surface, text_surface.get_rect()
def car(x,y):
    screen.blit(carimg,(x,y))

def obstacle(obs_x,obs_y,obs):  #definig function for obstacle
    if obs == 0:
        obs_pic = pygame.image.load("car2.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load("car3.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load("car4.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load("car5.jpg")
    elif obs == 4:
        obs_pic = pygame.image.load("car6.jpg")
    elif obs == 5:
        obs_pic = pygame.image.load("car7.jpg")
    screen.blit(obs_pic,(obs_x,obs_y))
    
def background():  #adding images to the background
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(377,0))
    screen.blit(yellow_strip,(377,100))
    screen.blit(yellow_strip,(377,200))
    screen.blit(yellow_strip,(377,300))
    screen.blit(yellow_strip,(377,400))
    screen.blit(yellow_strip,(377,500))
    screen.blit(yellow_strip,(377,600))
    screen.blit(strip,(120,0))
    screen.blit(strip,(679,0))

def countdown_background():
    # for event in pygame.event.get():
    #     pygame.quit()
    #     quit()
    #     # sys.exit()
    font = pygame.font.SysFont(None,35)
    x = (width*0.45)
    y = (height*0.8)
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(377,0))
    screen.blit(yellow_strip,(377,100))
    screen.blit(yellow_strip,(377,200))
    screen.blit(yellow_strip,(377,300))
    screen.blit(yellow_strip,(377,400))
    screen.blit(yellow_strip,(377,500))
    screen.blit(yellow_strip,(377,600))
    screen.blit(strip,(120,0))
    screen.blit(strip,(679,0))
    screen.blit(carimg,(x,y))
    passed = font.render("Passed : 0",True,(255,255,255))
    score = font.render("Score : 0",True,(0,0,0))
    screen.blit(passed,(0,50))
    screen.blit(score,(0,100))

def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        screen.fill((119,118,110))
        countdown_background()
        large_text = pygame.font.Font("freesansbold.ttf",115)
        text_surface,text_rect = text_object("3",large_text)
        text_rect.center = ((width/2),(height/2))
        screen.blit(text_surface,text_rect)
        pygame.display.update()
        clock.tick(1)

        screen.fill((119,118,110))
        countdown_background()
        large_text = pygame.font.Font("freesansbold.ttf",115)
        text_surface,text_rect = text_object("3",large_text)
        text_rect.center = ((width/2),(height/2))
        screen.blit(text_surface,text_rect)
        pygame.display.update()
        clock.tick(1)

        screen.fill((119,118,110))
        countdown_background()
        large_text = pygame.font.Font("freesansbold.ttf",115)
        text_surface,text_rect = text_object("2",large_text)
        text_rect.center = ((width/2),(height/2))
        screen.blit(text_surface,text_rect)
        pygame.display.update()
        clock.tick(1)

        screen.fill((119,118,110))
        countdown_background()
        large_text = pygame.font.Font("freesansbold.ttf",115)
        text_surface,text_rect = text_object("1",large_text)
        text_rect.center = ((width/2),(height/2))
        screen.blit(text_surface,text_rect)
        pygame.display.update()
        clock.tick(1)

        screen.fill((119,118,110))
        countdown_background()
        large_text = pygame.font.Font("freesansbold.ttf",115)
        text_surface,text_rect = text_object("GO!!!",large_text)
        text_rect.center = ((width/2),(height/2))
        screen.blit(text_surface,text_rect)
        pygame.display.update()
        clock.tick(1)

        countdown = False

        game_loop()        

def score_card(car_passed,score):
    font = pygame.font.SysFont(None,35)
    passed = font.render("Passed: " + str(car_passed), True, (255,255,255))
    score = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(passed, (0,50))
    screen.blit(score, (0,100))


def game_loop():  #defining game loop
    bumped=False  #close button
    x_change = 0
    x=375
    y=470
    obstacle_speed = 10
    obs = 0
    y_change = 0
    obs_x = random.randrange(200,650)
    obs_y = -750
    enemy_width = 56
    enemy_height = 125
    car_height = 125
    car_width = 56
    car_passed = 0
    score = 0
    level = 0

    # countdown_background()

    while not bumped:
        screen.fill((119,119,119))  #background colour
        background()  #adding grass
        obs_y -= (obstacle_speed/4)
        obstacle(obs_x,obs_y,obs)
        obs_y += obstacle_speed
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                bumped=True
            if event.type == pygame.KEYDOWN:  #moving the car in x or y direction
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_s:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
   
    
        car(x,y)    #calling car function
        score_card(car_passed,score)
        if x > 679 - car_width or x < 123:  #restricting the car movement
            screen.blit(render_text,(150,200))
            pygame.display.update()

            time.sleep(3)
            game_loop()

        if obs_y > height:  #randomizing enemy
            obs_y = 0 - enemy_height
            obs_x = random.randrange(170,width-170)
            obs = random.randrange(0,6)
            car_passed += 1
            score = car_passed * 10
            if int(car_passed) % 10 == 0:
                level += 1
                obstacle_speed += 2
                myfont = pygame.font.SysFont(None,100)
                level_text = myfont.render("Level: " + str(level), 1, (0,0,0))
                screen.blit(level_text,(265,50))
                pygame.display.update()
                time.sleep(3)

        if y < obs_y + enemy_height:  #crashing of enemy
            if x > obs_x and x < obs_x + car_width or x + car_width > obs_x and x + car_width < obs_x + car_width:
                print(x,obs_x,enemy_width)
                screen.blit(render_text,(150,200))
                pygame.display.update()
                time.sleep(3)
                game_loop()

        mouse = pygame.mouse.get_pos()  #creating pause button

        click = pygame.mouse.get_pressed()

        if mouse[0] > 650 and mouse[0] < 800 and mouse[1] > 0 and mouse[1] <50:  #colour of the buttons
            pygame.draw.rect(screen,blue2,(650,0,150,50))
            if click == (1,0,0):
                pause_page()
        else:
            pygame.draw.rect(screen,blue,(650,0,150,50))

        small_text = pygame.font.Font("freesansbold.ttf",30)
        text_surface,text_rect = text_object("PAUSE",small_text)
        text_rect.center = ((650+(150/2)),(0+(50/2)))
        screen.blit(text_surface,text_rect)

        pygame.display.update()  #updating the game 
        clock.tick(100)  #to slow down the speed of car


intro_loop()
game_loop()
pygame.quit()
quit()

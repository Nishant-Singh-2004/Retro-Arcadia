import pygame
from os.path import join
from random import randint ,uniform
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image=pygame.image.load(join('meteorBlaster','images','player.png')).convert_alpha()
        self.rect =self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.player_direction = pygame.math.Vector2()
        self.player_speed = 400
        #cooldown 
        self.can_shoot =True
        self.laser_shoot_time =0
        self.cooldown_duration = 400
        

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time -self.laser_shoot_time>=self.cooldown_duration:
                self.can_shoot=True
    
    def update(self,dt):
        #controlling speed and time
        keys = pygame.key.get_pressed()
        self.player_direction.x =int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.player_direction.y =int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        
        #makin player to stay inside the window
        if self.rect.bottomright[0]>=WINDOW_WIDTH:
            tempDirection = list(self.rect.bottomright)
            tempDirection[0]=WINDOW_WIDTH
            self.rect.bottomright=tuple(tempDirection)

        if self.rect.bottomleft[0]<=0:
            tempDirection = list(self.rect.bottomleft)
            tempDirection[0]=0
            self.rect.bottomleft=tuple(tempDirection)

        if self.rect.top<=0:
            self.rect.top=0

        if self.rect.bottom>=WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

        #maintaing speed    
        self.rect.center+=self.player_direction*self.player_speed*dt


       
        if int(keys[pygame.K_SPACE]) and self.can_shoot:
            
            self.can_shoot=False
            self.laser_shoot_time=pygame.time.get_ticks()
            laser_sound.play()
            Laser(playing_laser,self.rect.midtop,(all_sprites,laser_sprites))
            
        
        self.laser_timer()



class Star(pygame.sprite.Sprite):
    def __init__(self, groups,playing_star):
        super().__init__(groups)
        self.image =playing_star
        self.rect = self.image.get_frect(center=(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image=surf
        self.rect = self.image.get_frect(midbottom=pos)
    def update(self,dt):
        self.rect.centery-=400*dt
        if self.rect.bottom<0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image = surf
        self.rect=self.image.get_frect(center=pos)
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(400,500)
    def update(self,dt):
        global Player_Hit
        global score
        self.rect.center +=self.direction * self.speed * dt
        if WINDOW_HEIGHT<=self.rect.top<=WINDOW_HEIGHT+100 and not(Player_Hit):
            self.kill()
            score +=1


#display score:
def display_score():
    global score
    text_surf =font.render(str(score),True,(240,240,240))
    text_rect=text_surf.get_frect(midbottom=(WINDOW_WIDTH/2,WINDOW_HEIGHT-50))
    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface,(240,240,240),text_rect.inflate(20,20),5,10)


#collision 
def collision():
    global running
    global Player_Hit
    collision_player=pygame.sprite.spritecollide(player,meteor_sprites,True,pygame.sprite.collide_mask)
    if collision_player:
        Player_Hit=True
        damage_sound.play()
        game_music.fadeout(2000)
        pygame.time.delay(2000)
        reset_game()

    for laser in laser_sprites:
        spiritted_laser=pygame.sprite.spritecollide(laser , meteor_sprites,True)
        if spiritted_laser:
            explosion_sound.play()
            laser.kill()

#reseting game after being hit
def reset_game():
        global score
        global Player_Hit
        global running
        #timer

        display_surface.fill("gray0")
        score_title =large_text.render("Your Score : "+ str(score), True, (255, 255, 255))
        #spacebar_use = font.render("Press spacebar: Start Game",True, (255, 255, 255))
        #esc_use = font.render("Press ESC: End game",True, (255, 255, 255))
        score=0

        text_rect=score_title.get_frect(midbottom=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2-60))
        #text_spacbar = spacebar_use.get_frect(midbottom=((WINDOW_WIDTH/2,WINDOW_HEIGHT/2+30)))
        #text_esc = esc_use.get_frect(midbottom=((WINDOW_WIDTH/2,WINDOW_HEIGHT/2+120)))

        pygame.draw.rect(display_surface,(240,240,240),text_rect.inflate(20,20),5,10)
        #pygame.draw.rect(display_surface,(240,240,240),text_spacbar.inflate(20,20),5,10)
        #pygame.draw.rect(display_surface,(240,240,240),text_esc.inflate(20,20),5,10)

        display_surface.blit(score_title,text_rect)
        #display_surface.blit(spacebar_use,text_spacbar)
        #display_surface.blit(esc_use,text_esc)
        pygame.display.update()

        pygame.time.delay(3000)
        Player_Hit=False
        game_music.play()
        



        

#general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("space shooter")
running = True

#imports
#images
playing_star=pygame.image.load(join('meteorBlaster','images','star.png')).convert_alpha()
playing_meteor = pygame.image.load(join('meteorBlaster','images','meteor.png')).convert_alpha()
playing_laser = pygame.image.load(join('meteorBlaster','images','laser.png')).convert_alpha()
#fonts
font =pygame.font.Font(join('meteorBlaster',"images","Oxanium-Bold.ttf"),30)
large_text = pygame.font.Font(join('meteorBlaster',"images","Oxanium-Bold.ttf"),70)
#audio files
laser_sound =pygame.mixer.Sound(join('meteorBlaster','space shooter files','audio','laser.wav'))
explosion_sound =pygame.mixer.Sound(join('meteorBlaster','space shooter files','audio','explosion.wav'))
damage_sound =pygame.mixer.Sound(join('meteorBlaster','space shooter files','audio','damage.ogg'))
game_music =pygame.mixer.Sound(join('meteorBlaster','space shooter files','audio','game_music.wav'))
game_music.play()
game_music.set_volume(0.7)
explosion_sound.set_volume(0.4)
laser_sound.set_volume(0.5)


#calculating time for score generation
score =0
Player_Hit =False


#sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(25):
    Star(all_sprites,playing_star)
player =Player(all_sprites)



#custom event->meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event,300)

while running:
    dt=clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display_surface.exit()
            running = False
        if event.type==meteor_event:
            x,y = randint(0,WINDOW_WIDTH),randint(-200,-100)
            Meteor(playing_meteor,(x,y),(all_sprites,meteor_sprites))
    display_surface.fill("gray0")
    #update
    all_sprites.update(dt)
    #collision
    collision()
    all_sprites.draw(display_surface)
    display_score()
    
    pygame.display.update()


pygame.quit()
        
import pygame
from os.path import join
from random import randint ,uniform
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image=pygame.image.load(join('images','player.png')).convert_alpha()
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
        self.rect.center+=self.player_direction*self.player_speed*dt

       
        if int(keys[pygame.K_SPACE]) and self.can_shoot:
            
            self.can_shoot=False
            self.laser_shoot_time=pygame.time.get_ticks()
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
        self.rect.center +=self.direction * self.speed * dt
        if self.rect.top>WINDOW_HEIGHT:
            self.kill()

#display score:
def display_score():
    current_time =pygame.time.get_ticks()//100
    text_surf =font.render(str(current_time),True,(240,240,240))
    text_rect=text_surf.get_frect(midbottom=(WINDOW_WIDTH/2,WINDOW_HEIGHT-50))
    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface,(240,240,240),text_rect.inflate(20,20),5,10)


#collision 
def collision():
    global running
    collision_player=pygame.sprite.spritecollide(player,meteor_sprites,True,pygame.sprite.collide_mask)
    if collision_player:
        running =False
    for laser in laser_sprites:
        spiritted_laser=pygame.sprite.spritecollide(laser , meteor_sprites,True)
        if spiritted_laser:
            laser.kill()

#general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("space shooter")
running = True

#imports
playing_star=pygame.image.load(join('images','star.png')).convert_alpha()
playing_meteor = pygame.image.load(join('images','meteor.png')).convert_alpha()
playing_laser = pygame.image.load(join('images','laser.png')).convert_alpha()
font =pygame.font.Font(join("images","Oxanium-Bold.ttf"),30)
explosion_frames = [pygame.image.load(join("images","explosion",f"{i}.png")).convert_alpha() for i in range(21)]

#sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites,playing_star)
player =Player(all_sprites)



#custom event->meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event,500)

while running:
    dt=clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==meteor_event:
            x,y = randint(0,WINDOW_WIDTH),randint(-200,-100)
            Meteor(playing_meteor,(x,y),(all_sprites,meteor_sprites))
    display_surface.fill("black")
    #update
    all_sprites.update(dt)
    #collision
    collision()
    all_sprites.draw(display_surface)
    display_score()
    
    pygame.display.update()


pygame.quit()

import pygame, math, sys
from pygame.locals import *
track = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()
####DA CAR####
class CarSprite(pygame.sprite.Sprite):
        ACELLERATION = 2
        MAX_FORWARD_SPEED = 10
        MAX_REVERSE_SPEED = -5
        TURN_SPEED=5
        
        def __init__(self,image,position):
                pygame.sprite.Sprite.__init__(self)
                self.src_image = pygame.image.load(image)
                self.k_up = self.k_down = self.k_right = self.k_left = 0
                self.speed = self.direction = 0
                self.position = position

        def update(self,deltat):
                self.speed +=(self.k_up+self.k_down)
                if self.speed > self.MAX_FORWARD_SPEED:  self.speed = self.MAX_FORWARD_SPEED
                if self.speed < self.MAX_REVERSE_SPEED:  self.speed = self.MAX_REVERSE_SPEED
                self.direction +=(self.k_right+self.k_left)
                x,y=self.position
                rad = self.direction*math.pi/180
                x+=-self.speed*math.sin(rad)
                y+=-self.speed*math.cos(rad)
                self.position=(x,y)
                self.image=pygame.transform.rotate(self.src_image,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=self.position
                
####DA PADS####
class PadSprite(pygame.sprite.Sprite):
        normal=pygame.image.load('pad_normal.png')
        hit=pygame.image.load('pad_hit.png')
        def __init__(self,number,position):
                self.number=number
                self.rect=pygame.Rect(self.normal.get_rect())
                self.rect.center=position
                self.image=self.normal
pad_group = [PadSprite(1,(200,200)),PadSprite(2,(800,200)),PadSprite(3,(200,600)),PadSprite(4,(800,600))]
current_pad_number = 0
BLACK = (0,0,0)
rect = track.get_rect()
car = CarSprite('car.png',rect.center)
car_group=pygame.sprite.RenderPlain(car)
####DA ANIMATION###
while True:
        deltat = clock.tick(30)
        for event in pygame.event.get():
                if not hasattr(event,'key'): continue
                down = event.type == KEYDOWN
                if event.key ==K_RIGHT : car.k_right = down * -5
                if event.key ==K_LEFT : car.k_left = down * 5
                if event.key ==K_UP : car.k_up = down * 2
                if event.key ==K_DOWN : car.k_down = down * -2
                if event.key ==K_ESCAPE : sys.exit(0)
        track.fill(BLACK)
        pads = pygame.sprite.spritecollide(car,pad_group,False)
        if pads:
                pad = pads[0]
                if pad.number == current_pad_number + 1:
                        pad.image=pad.hit
                        current_pad_number+=1
                elif current_pad_number==4:
                        for pad in pad_group.sprites(): pad.image = pad.normal
                        current_pad_number=0
        car_group.update(deltat)
        car_group.draw(track)
        pygame.display.flip()

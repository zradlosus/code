import pygame
import sys
from pygame.sprite import Sprite, Group
from config import config
from time import sleep
import random as r

pygame.init()

def game_over():
    sys.exit()
pygame.display.set_caption("Samo Dash")
pygame.display.set_icon(pygame.image.load("assets/ikona 1.png"))
            
class Cube(Sprite):
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.CUBE_IMAGE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = 150
        self.rect[1] = 800
        self.speed = config.CUBE_SPEED
        self.jump_power = config.CUBE_JUMP_POV
        
    def update(self, config):
        self.rect[1] = self.rect[1] + self.speed
        self.speed +=1
    
    def stop(self):
        self.speed = 0

class Floor(Sprite):
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.FLOOR_IMAGE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 900
        self.image = pygame.transform.scale(self.image, (1500, 1000))
        self.speed = config.FLOOR_SPEED
    
    def update(self):
        self.rect[0] -= self.speed
        if self.rect[0] < -450:
            self.rect[0] = 0
        
class Spike(Sprite):
    def __init__(self, config, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.SPIKE_IMG).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.speed = floor.speed
        
    def update(self):
        self.rect[0] -= self.speed
        
class Dvakrat(Sprite):
    def __init__(self, config, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.DVA_IMG).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.speed = floor.speed
        
    def update(self):
        self.rect[0] -= self.speed
        
class Trikrat(Sprite):
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.TRI_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = config.TRI_POS[0]
        self.rect[1] = config.TRI_POS[1]
        self.speed = floor.speed
        
    def update(self):
        self.rect[0] -= self.speed
        
class Block(Sprite):
    def __init__(self, config, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.BLOCK_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.BLOCK_SIZE[0], config.BLOCK_SIZE[1]))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.speed = floor.speed
        
    def update(self):
        self.rect[0] -= self.speed
        
class L_EDIT_BUTT(Sprite):
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.L_ED_BUTT_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = 500
        self.rect[1] = 500
        

class CC(Sprite):
    def __init__(self, config, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.CC_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (config.CC_SIZE[0], config.CC_SIZE[1]))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.speed = floor.speed
        
    def update(self):
        self.rect[0] -= self.speed
        
class Finish(Sprite):
    def __init__(self, config, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.FINISH_IMAGE).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
        self.speed = floor.speed
        
    def update(self):
        if win == False:
            self.rect[0] -= self.speed
        
        
def check_colizion_dead(obj1, obj2):
    if pygame.sprite.groupcollide(obj1, obj2, False, False, pygame.sprite.collide_mask):
        print("hehehe")
        game_over()
        
def check_colizion_stop(obj1, jump):
    for obj in strong_objects_grs:
        if pygame.sprite.groupcollide(obj1, obj, False, False, pygame.sprite.collide_mask):
            jump = False
            cube.stop()
        if jump != False:
            jump = True
    return jump
        
def check_colizion_sped(obj1, obj2, sped):
    if pygame.sprite.groupcollide(obj1, obj2, False, False, pygame.sprite.collide_mask):
        for o in objects:
            o.speed = sped
            cube.jump_power = 20

 
def check_collizion_win(obj, obj2):
    if pygame.sprite.groupcollide(obj, obj2, False, False, pygame.sprite.collide_mask):       
        return True
    else: 
        return False  

def create_spike(pos):
    spike = Spike(config, pos)
    spike.add(spike_group)
    objects.append(spike)
    
def two_time_create_speed_change(config, pos):
    dva = Dvakrat(config, pos)
    dva.add(dva_group)
    objects.append(dva)
    
def create_cube(pos, have_cc):
    block = Block(config, pos)
    if have_cc:
        create_cc([pos[0], pos[1] -15], config)
    block.add(block_group)
    objects.append(block)

def create_2X3_block(start):
    create_cube([start, 860], False)
    create_cube([start, 820], True)
    create_cube([start + 50, 860], False)
    create_cube([start + 50, 820], True)
    create_cube([start + 100, 860], False)
    create_cube([start + 100, 820], True)
    
def create_cc(pos, config):
    cc = CC(config, pos)
    cc.add(cc_group)
    strong_objects_grs.append(cc_group)
    objects.append(cc)

    
def new_level(level):
    if level == 1:
        create_spike([600, 860])
        create_spike([900, 860])
        create_spike([1300, 860])
        create_cube([1800, 860], True)
        create_cube([2100, 800], True)
        create_cube([2400, 750], True)
        create_spike([1900, 860])
        create_spike([2000, 860])
        create_spike([2100, 860])
        create_spike([2200, 860])
        create_spike([2300, 860])
        create_spike([2400, 860])
        create_spike([2500, 860])
        create_cc([2600, 890], config)
        create_spike([2900, 860])
        create_spike([2950, 860])
        create_2X3_block(3300)
        create_2X3_block(3700)
        create_2X3_block(4100)
        finish = Finish(config, [4500, 700])
        objects.append(finish)
        finish.add(finish_group)
    if level == 2:
        cube.rect[1] == 800
        create_spike([600, 850])
        create_spike([640, 850])
        create_spike([680, 850])
        two_time_create_speed_change(config, [800, 850])
        for a in range(1000, 1300, 50):
            create_spike([a, 850])
        create_cube([1200, 830], True)
        for a in range(1700, 1900, 50):
            create_spike([a, 850])
        create_cube([2300, 830], True)
        create_cube([2700, 800],True)
        create_cube([2900, 830], True)
        create_cube([3300, 800], True)
        create_cube([3450, 830], True)
        create_cube([3500, 830], True)
        create_cube([3550, 830], True)
        create_cube([3600, 830], True)
        create_cube([3650, 830], True)
        create_spike([3650, 770])
        finish = Finish(config, [4000, 700])
        objects.append(finish)
        finish.add(finish_group)

if __name__ == "__main__":
    level = 1
    win = False
    screen = pygame.display.set_mode((1000, 1000))

    floor = Floor(config)
    floor_group = Group([floor])
    
    finish_group = Group([])
    
    cube = Cube(config)
    cube_group = Group([cube])
    
    spike = Spike(config, [1333, 3123])
    spike_group = Group([])
    
    block = Block(config, [128, 2110])
    block_group = Group([block])
    
    cc = CC(config, [1212, 1312])
    cc_group = Group([cc])
    
    dva_group = Group([])
    
    all_groups = [cube_group, spike_group, block_group, cc_group, dva_group, finish_group]
    
    clock = pygame.time.Clock()
    jump = False
    chance_spike = 100
    objects = [spike, floor, cc]
    strong_objects_grs = [floor_group, cc_group]
    new_level(level)
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if jump == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(3):
                        cube.speed = -config.CUBE_JUMP_POV
                        jump = True
                
        screen.fill(pygame.color.Color(51, 204, 255))
                
        floor_group.draw(screen)
        finish_group.draw(screen)
        cube_group.draw(screen)
        spike_group.draw(screen)
        block_group.draw(screen)
        cc_group.draw(screen)
        dva_group.draw(screen)
        if win:
            screen.blit(pygame.image.load(config.WIN_BG_IMAGE), (0, 0))
            for a in range(504, 682):
                if pygame.mouse.get_pos()[0] == a:
                    for b in range(682, 771):
                        if pygame.mouse.get_pos()[1] == b and pygame.mouse.get_pressed(3):
                            for gr in all_groups:
                                for obj in gr:
                                    if obj != cube:
                                        obj.remove(gr)
                            win = False
                            new_level(2)
        for fin in finish_group:
            fin.update()
        
        clock.tick(config.GAME_FPS)
        pygame.display.update()
        cube.update(config)
        floor.update()
        block.update()
        cc.update()
        
        for dva in dva_group:
            dva.update()

        for sp in spike_group:
            sp.update()
            if sp.rect[0] <= 0:
                sp.remove(spike_group)
                
        for blo in block_group:
            blo.update()
        for cs in cc_group:
            cs.update()
        check_colizion_dead(cube_group, spike_group)
        check_colizion_dead(cube_group, block_group)
        
        check_colizion_sped(cube_group, dva_group, config.SPPED_2)
        
        win = check_collizion_win(cube_group, finish_group)
        
        jump = check_colizion_stop(cube_group, jump)
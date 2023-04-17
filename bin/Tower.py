import pygame
import pygame.gfxdraw
import math
from .settings import *
from .Enemy import Enemy
from .ringShot import RingShotSprite

class Tower(pygame.sprite.Sprite):
    def __init__(self, 
        group, 
        pos:pygame.math.Vector2, 
        enemy_group:pygame.sprite.Group, 
        animation_group:pygame.sprite.Group,
        type:str
    ) -> None:
        super().__init__(group)

        self.type = type
        self.pos = pos
        self.color = TOWER_BASEVALUES[self.type]["color"]
        
        self.range = TOWER_BASEVALUES[self.type]["range"]
        self.height, self.width = self.range*2,self.range*2
        
        self.image = pygame.Surface([self.width,self.height],pygame.SRCALPHA)
        # self.image.fill("white")
        # self.image.set_colorkey("white")
        self.rect = self.image.get_rect(center=self.pos)
        pygame.draw.circle(self.image,self.color,(self.range,self.range),25)
        # pygame.gfxdraw.filled_circle(self.image,32,32,12,(0,255,255))
        # self.display_surface = pygame.display.get_surface()

        self.animation_group = animation_group

        self.enemy_group = enemy_group
        self.enemies_in_range = []
        self.can_shoot = True
        self.time_of_last_shot = pygame.time.get_ticks()
        self.attack_delay = TOWER_BASEVALUES[self.type]["attack_delay"] #ms
        # self.range = 200
        #draw range
        pygame.gfxdraw.aacircle(self.image,self.range-1,self.range-1,self.range,(50,50,50))
        self.damage = TOWER_BASEVALUES[self.type]["damage"]
        self.splash_radius = 0 if not "splash_radius" in TOWER_BASEVALUES[self.type].keys() else TOWER_BASEVALUES[self.type]["splash_radius"]
        self.has_splash = True if self.splash_radius > 0 else False

        self.target_strategy = TOWER_BASEVALUES[self.type]["target_strategy"]

    def findEnemiesInRange(self):
        #get enemies in range, descending from furthest enemy
        self.enemies_in_range = []
        if not self.can_shoot:
            return
        # for enemy in sorted(self.enemy_group.sprites(),key=lambda x:x.percent_of_path_traveled,reverse=True):
        for enemy in self.enemy_group.sprites():
            if Tower.inRange(self.pos,enemy,self.range):
                self.enemies_in_range.append(enemy)
        # print(self.enemies_in_range)

    @staticmethod
    def inRange(pos:pygame.math.Vector2,enemy:Enemy,radius:float):
        if math.sqrt((pos.x - enemy.pos.x)**2 + (pos.y - enemy.pos.y)**2) < radius:
            return True
        else:
            return False
    
    def shootAtEnemy(self):
        if not self.can_shoot:
            if self.time_of_last_shot + self.attack_delay < pygame.time.get_ticks():
                self.can_shoot = True
            else:
                return
        # find all enemies in range
        self.findEnemiesInRange()
        #shoot at point
        if len(self.enemies_in_range) == 0:
            #nothing to shoot
            return
        if self.target_strategy == "first":
            enemy_to_shoot_at = sorted(self.enemies_in_range,key=lambda x:x.percent_of_path_traveled,reverse=True)[0]
        elif self.target_strategy == "strongest":
            enemy_to_shoot_at = sorted(self.enemies_in_range,key=lambda x:x.health,reverse=True)[0]
        if self.has_splash:
            for enemy in self.enemy_group.sprites():
                if Tower.inRange(enemy_to_shoot_at.pos,enemy,self.splash_radius):
                    enemy.changeHealth(-self.damage)
        else:
            enemy_to_shoot_at.changeHealth(-self.damage)
        if self.has_splash:
            RingShotSprite(self.animation_group,enemy_to_shoot_at.pos,radius=self.splash_radius,color=self.color)
        else:
            RingShotSprite(self.animation_group,enemy_to_shoot_at.pos,color=self.color)
        print("Pow!")

        self.can_shoot = False
        self.time_of_last_shot = pygame.time.get_ticks()

    # def draw(self):
    #     pygame.draw.circle(self.image,"blue",self.pos,25)

    def update(self,dt):
        # pygame.draw.circle(self.image,"blue",self.pos,25)
        self.shootAtEnemy()
        pass
        
        # print(self.pos.x, self.pos.y)




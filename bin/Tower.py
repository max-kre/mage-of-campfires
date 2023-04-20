import pygame
import pygame.gfxdraw
import math
from .settings import *
from .Enemy import Enemy
from .ringShot import RingShotSprite
from .utils.utility_funcs import *

IMAGES = {
    "blast": pygame.image.load('data/graphics/towers/cannon_lvl1.png'),
    "sniper": pygame.image.load('data/graphics/towers/cannon_lvl1.png')
}
FOUNDATION_IMG = pygame.image.load('data/graphics/towers/foundation.png')
class Tower(pygame.sprite.Sprite):
    def __init__(self, 
        group, 
        pos:pygame.math.Vector2, 
        enemy_group:pygame.sprite.Group, 
        animation_group:pygame.sprite.Group,
        type:str, 
    ) -> None:
        super().__init__(group)

        self.type = type
        self.pos = pos
        self.color = TOWER_BASEVALUES[self.type]["color"]
        
        self.range = TOWER_BASEVALUES[self.type]["range"]
        self.height, self.width = self.range*2, self.range*2
        
        self.foundation = FOUNDATION_IMG
        # self.pos_f = (pos[0]-10, pos[1]-10)
        # self.rect_f = self.foundation.get_rect(center=self.pos_f)

        self.base_image = pygame.Surface([self.width, self.height],pygame.SRCALPHA)
        # self.image_canon = pygame.image.load('data/graphics/towers/cannon_lvl1.png').convert_alpha()
        self.base_image.blit(self.foundation, (self.range-self.foundation.get_width()//2, self.range-self.foundation.get_height()//2))
        pygame.draw.circle(self.base_image,self.color,(self.range, self.range),self.range,width=1)
        # self.image.fill("white")
        # self.image.set_colorkey("white")
        self.image=self.base_image.copy()
        self.rect = self.image.get_rect(center=self.pos)
        #pygame.draw.circle(self.image,self.color,(self.range,self.range),25)
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
        # pygame.gfxdraw.aacircle(self.image,self.range-1,self.range-1,self.range,(50,50,50))
        self.damage = TOWER_BASEVALUES[self.type]["damage"]
        self.splash_radius = 0 if not "splash_radius" in TOWER_BASEVALUES[self.type].keys() else TOWER_BASEVALUES[self.type]["splash_radius"]
        self.has_splash = True if self.splash_radius > 0 else False
        self.effects = {
            "spawn_secondary":{
                "damage": self.damage//2,
                "radius": self.splash_radius//2,
                "effect": {
                    "spawn_secondary":{
                        "damage": self.damage//3,
                        "radius": self.splash_radius//3,
                        "effect": None
                    }
                }
            }
        }

        self.target_strategy = TOWER_BASEVALUES[self.type]["target_strategy"]

    def findEnemiesInRange(self):
        #get enemies in range, descending from furthest enemy
        self.enemies_in_range = []
        if not self.can_shoot:
            return
        # for enemy in sorted(self.enemy_group.sprites(),key=lambda x:x.percent_of_path_traveled,reverse=True):
        for enemy in self.enemy_group.sprites():
            if enemyInRange(self.pos,enemy.pos,self.range):
                self.enemies_in_range.append(enemy)
        # print(self.enemies_in_range)

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
        # self.dealDamage(enemy_to_shoot_at)
        self.spawnDamageEffect(enemy_to_shoot_at)
        self.rotateTowerImage(enemy_to_shoot_at.pos)

    def spawnDamageEffect(self, enemy_to_shoot_at):
        if self.has_splash:
            RingShotSprite(self.animation_group,enemy_to_shoot_at.pos,self.enemy_group,damage=self.damage,effect_status=self.effects,radius=self.splash_radius,color=self.color)
        else:
            RingShotSprite(self.animation_group,enemy_to_shoot_at.pos,self.enemy_group,damage=self.damage,effect_status=None,color=self.color)
        print("Pow!")

        self.can_shoot = False
        self.time_of_last_shot = pygame.time.get_ticks()

    def dealDamage(self,enemy_to_shoot_at):
        if self.has_splash:
            for enemy in self.enemy_group.sprites():
                if enemyInRange(enemy_to_shoot_at.pos,enemy.pos,self.splash_radius):
                    enemy.changeHealth(-self.damage)
        else:
            enemy_to_shoot_at.changeHealth(-self.damage)
        pass

    def rotateTowerImage(self, enemy_pos:pygame.math.Vector2):
        delta_x = enemy_pos.x - self.pos.x
        delta_y = enemy_pos.y - self.pos.y
        angle_to_enemy = -90+math.degrees(math.atan2(-delta_y,delta_x))
        rot_image = pygame.transform.rotate(IMAGES[self.type],angle_to_enemy)
        self.image = self.base_image.copy()
        self.image.blit(
            rot_image,
            (self.range - rot_image.get_width()//2, self.range - rot_image.get_height()//2)
        )
        pass

    # def draw(self):
    #     pygame.draw.circle(self.image,"blue",self.pos,25)

    def update(self,dt):
        # pygame.draw.circle(self.image,"blue",self.pos,25)
        self.shootAtEnemy()
        pass
        
        # print(self.pos.x, self.pos.y)




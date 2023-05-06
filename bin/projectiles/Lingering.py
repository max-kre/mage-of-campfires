import pygame
# import pygame.gfxdraw
from ..utils.utility_funcs import *


class LingeringEffect(pygame.sprite.Sprite):
    def __init__(self, groups, pos, enemies:pygame.sprite.Group, damage, effect_status:dict=None, radius=None, color=None) -> None:
        super().__init__(groups)
        self.sprite_groups = groups #for spawnSecondary
        self.enemies = enemies
        self.pos = pos
        print(pos)
        self.color = color if color else (50,255,50)
        self.init_time = pygame.time.get_ticks()
        self.animation_time = 2000 #ms
        self.radius = radius if radius else 50
        self.damage = damage # DPS
        self.status = effect_status
        self.image = pygame.Surface([self.radius*2, self.radius*2],pygame.SRCALPHA)
        pygame.draw.circle(self.image,self.color,(self.radius,self.radius),self.radius)
        self.rect = self.image.get_rect(center=self.pos)
        self.printDmg = True

    def update(self,dt):
        # scaling_factor = (pygame.time.get_ticks() - self.init_time) / self.animation_time
        if pygame.time.get_ticks() > self.init_time + self.animation_time:
            self.kill()
            return

        self.dealDamageToEnemies(dt)

        # pygame.gfxdraw.circle(self.image,self.max_radius,self.max_radius,r,self.color)
        # pygame.gfxdraw.filled_circle(self.image,self.max_radius,self.max_radius,r,(123,20,20))
        # self.image.set_alpha(125)

    def dealDamageToEnemies(self,dt):
        for enemy in self.enemies.sprites():
            if self.rect.colliderect(enemy.rect):
                if self.printDmg:
                    print(-self.damage * dt,dt)
                    self.printDmg=False
                enemy.changeHealth(-self.damage * dt) #
                if self.status:
                    self.applyEffects(enemy)


    def applyEffects(self,enemy):
        if "spawn_explosion" in self.status.keys():
            self.spawnSecondary(self.sprite_groups,enemy.pos,self.enemies,self.status["spawn_explosion"]["damage"],self.status["spawn_explosion"]["effect"],self.status["spawn_explosion"]["radius"],"blue")#self.color)
        if "slow" in self.status.keys():
            enemy.handleEffects("slow",start=True,info_dict=self.status["slow"])
        
    
    def spawnSecondary(self,groups,pos:pygame.math.Vector2,enemies,effect_damage,effect_status,radius,color):
        # RingShotSprite(groups,pos,enemies,effect_damage,effect_status,radius,color)
        pass

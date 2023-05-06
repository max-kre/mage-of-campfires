import pygame
# import pygame.gfxdraw
from ..utils.utility_funcs import *


class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, pos, enemies:pygame.sprite.Group, damage, effect_status:dict=None, radius=None, color=None) -> None:
        super().__init__(groups)
        self.sprite_groups = groups #for spawnSecondary
        self.enemies = enemies
        self.pos = pos
        print(pos)
        self.color = color if color else (255,50,50)
        self.init_time = pygame.time.get_ticks()
        self.animation_time = 200 #ms
        self.max_radius = radius if radius else 25
        self.already_damaged = []
        self.damage = damage
        self.status = effect_status
        self.image = pygame.Surface([self.max_radius*2, self.max_radius*2],pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self,dt):
        scaling_factor = (pygame.time.get_ticks() - self.init_time) / self.animation_time
        if scaling_factor > 1:
            self.kill()
            return
        self.image = pygame.Surface([self.max_radius*2, self.max_radius*2],pygame.SRCALPHA)
        r = int(scaling_factor * self.max_radius)

        self.dealDamageToEnemies(r)

        # pygame.gfxdraw.circle(self.image,self.max_radius,self.max_radius,r,self.color)
        pygame.draw.circle(self.image,self.color,(self.max_radius,self.max_radius),r,1)
        # pygame.gfxdraw.filled_circle(self.image,self.max_radius,self.max_radius,r,(123,20,20))
        # self.image.set_alpha(125)

    def dealDamageToEnemies(self,current_r):
        for enemy in self.enemies.sprites():
            if enemyInRange(self.pos,enemy.pos,current_r) and not enemy in self.already_damaged:
                enemy.changeHealth(-self.damage)
                if self.status:
                    self.applyEffects(enemy)
                self.already_damaged.append(enemy)

    def applyEffects(self,enemy):
        if "spawn_secondary" in self.status.keys():
            self.spawnSecondary(self.sprite_groups,enemy.pos,self.enemies,self.status["spawn_secondary"]["damage"],self.status["spawn_secondary"]["effect"],self.status["spawn_secondary"]["radius"],"blue")#self.color)
    
    def spawnSecondary(self,groups,pos:pygame.math.Vector2,enemies,effect_damage,effect_status,radius,color):
        Explosion(groups,pos,enemies,effect_damage,effect_status,radius,color)
        # pass


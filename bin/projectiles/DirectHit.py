import pygame
import math
from .Lingering import LingeringEffect
from .Explosion import Explosion
# import pygame.gfxdraw
from ..utils.utility_funcs import *

class DirectHit(pygame.sprite.Sprite):
    def __init__(self, groups, pos:pygame.math.Vector2, enemies:pygame.sprite.Group, enemy, damage, effect_status:dict=None, color=None) -> None:
        super().__init__(groups)
        self.sprite_groups = groups #for spawnSecondary
        self.enemies = enemies
        self.startpos = pos.copy()
        self.pos = pos.copy() #pygame.math.Vector2(startpos.x,startpos.y)
        self.target_enemy = enemy
        self.color = color if color else (50,50,50)
        self.speed = 1300
        self.damage = damage
        self.status = effect_status
        self.image = pygame.Surface([10, 10],pygame.SRCALPHA)
        pygame.draw.circle(self.image,self.color,(5,5),5,5)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self,dt):
        self.move(dt)
        if self.rect.colliderect(self.target_enemy.rect):
        # if calcLengthBetweenPos(self.startpos,self.pos) > calcLengthBetweenPos(self.startpos, self.target_enemy.pos):
            # if bullet behind enemy from POV of tower
            self.dealDamageToEnemy()
            self.kill()
            # return

    def move(self, dt):
        direction = pygame.math.Vector2(
            self.target_enemy.pos - self.pos
        ).normalize()
        self.pos += direction * self.speed * dt
        self.rect.center = self.pos
        pass

    def dealDamageToEnemy(self):
        self.target_enemy.changeHealth(-self.damage)
        if self.status:
            self.applyEffects(self.target_enemy)

    def applyEffects(self,enemy):
        if "spawn_explosion" in self.status.keys():
            # self.spawnSecondary(self.sprite_groups,enemy.pos,self.enemies,self.status["spawn_explosion"]["damage"],self.status["spawn_explosion"]["effect"],self.status["spawn_explosion"]["radius"],"blue")#self.color)
            Explosion(self.sprite_groups,enemy.pos,self.enemies,self.status["spawn_explosion"]["damage"],self.status["spawn_explosion"]["effect"],self.status["spawn_explosion"]["radius"],self.color)
        if "create_puddle" in self.status.keys():
            LingeringEffect(self.sprite_groups,enemy.pos,self.enemies,self.status["create_puddle"]["damage"],effect_status=self.status["create_puddle"]["effect"],radius=self.status["create_puddle"]["radius"],color=self.color)#self.color)

    # def spawnSecondary(self,groups,pos:pygame.math.Vector2,enemies,effect_damage,effect_status,radius,color):
    #     # Explosion(groups,pos,enemies,effect_damage,effect_status,radius,color)
    #     pass


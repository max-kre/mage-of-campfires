import pygame
# from .Explosion import Explosion
# from .DirectHit import DirectHit
from ..utils.utility_funcs import *


class LingeringEffect(pygame.sprite.Sprite):
    def __init__(self, groups, pos, enemies:pygame.sprite.Group, damage=None, effect_status:dict=None, radius=None, duration_ms=None,color=None, parent=None) -> None:
        super().__init__(groups)
        self.parent=parent
        self.sprite_groups = groups #for spawnSecondary
        self.enemies = enemies
        self.pos = pos
        # print(pos)
        self.color = color if color else (50,255,50)
        self.init_time = pygame.time.get_ticks()
        self.duration = duration_ms if duration_ms else 2000 #ms
        self.radius = radius if radius else 50
        self.damage = damage if damage else 0 #DPS
        self.status = effect_status if effect_status else {}
        self.image = pygame.Surface([self.radius*2, self.radius*2],pygame.SRCALPHA)
        pygame.draw.circle(self.image,self.color,(self.radius,self.radius),self.radius)
        self.image.set_alpha(175)
        self.rect = self.image.get_rect(center=self.pos)
        # self.printDmg = True

    def update(self,dt):
        # scaling_factor = (pygame.time.get_ticks() - self.init_time) / self.duration
        if pygame.time.get_ticks() > self.init_time + self.duration:
            self.kill()
            return

        self.dealDamageToEnemies(dt)

        # pygame.gfxdraw.circle(self.image,self.max_radius,self.max_radius,r,self.color)
        # pygame.gfxdraw.filled_circle(self.image,self.max_radius,self.max_radius,r,(123,20,20))
        # self.image.set_alpha(125)

    def dealDamageToEnemies(self,dt):
        for enemy in self.enemies.sprites():
            if self.rect.colliderect(enemy.rect):
                # if self.printDmg:
                #     print(-self.damage * dt,dt)
                #     self.printDmg=False
                enemy.changeHealth(-self.damage * dt) #
                if self.status:
                    self.applyEffects(enemy)


    def applyEffects(self,enemy):
        self.parent.handle_effects(self, enemy)


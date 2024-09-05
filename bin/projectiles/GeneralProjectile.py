from .Explosion import Explosion
from .Lingering import LingeringEffect
from .DirectHit import DirectHit
import pygame

class GeneralProjectile:
    def __init__(self, projectile_type, groups, pos, enemies:pygame.sprite.Group, enemy=None, damage=None, effect_status:dict=None,radius=None, duration_ms=None, color=None) -> None:
        self.sprite_groups = groups
        self.enemies = enemies
        if projectile_type == "Explosion":
            self.projectile = Explosion(groups, pos, enemies, damage, effect_status, radius, duration_ms, color, parent=self)
        elif projectile_type == "LingeringEffect":
            self.projectile = LingeringEffect(groups, pos, enemies, damage, effect_status, radius, duration_ms, color, parent=self)
        elif projectile_type == "DirectHit":
            self.projectile = DirectHit(groups, pos, enemies, enemy, damage, effect_status, color, parent=self)

    def handle_effects(self, calling_projectile, enemy):
        #def applyEffects(self,enemy):
        if "spawn_explosion" in calling_projectile.status.keys():
            k = "spawn_explosion"
            damage = calling_projectile.status[k]["damage"] if "damage" in dict.keys(calling_projectile.status[k]) else None
            effect_status = calling_projectile.status[k]["effect"] if "effect" in dict.keys(calling_projectile.status[k]) else None
            radius = calling_projectile.status[k]["radius"] if "radius" in dict.keys(calling_projectile.status[k]) else None
            duration = effect_status[k]["duration"] if "duration" in dict.keys(calling_projectile.status[k]) else None
            color = calling_projectile.status[k]["color"] if "color" in dict.keys(calling_projectile.status[k]) else calling_projectile.color
            Explosion(self.sprite_groups,enemy.pos,self.enemies,damage=damage,effect_status=effect_status,radius=radius,duration_ms=duration,color=color, parent=self)
        if "create_puddle" in calling_projectile.status.keys():
            k = "create_puddle"
            damage = calling_projectile.status[k]["damage"] if "damage" in dict.keys(calling_projectile.status[k]) else None
            effect_status = calling_projectile.status[k]["effect"] if "effect" in dict.keys(calling_projectile.status[k]) else None
            radius = calling_projectile.status[k]["radius"] if "radius" in dict.keys(calling_projectile.status[k]) else None
            duration = calling_projectile.status[k]["duration"] if "duration" in dict.keys(calling_projectile.status[k]) else None
            color = calling_projectile.status[k]["color"] if "color" in dict.keys(calling_projectile.status[k]) else calling_projectile.color
            LingeringEffect(self.sprite_groups,enemy.pos,self.enemies,damage=damage,effect_status=effect_status,radius=radius,duration_ms=duration,color=color, parent=self)#self.color)
        if "slow" in calling_projectile.status.keys():
            enemy.handleEffects("slow",start=True,info_dict=calling_projectile.status["slow"])
        


    #self, groups, pos, enemies:pygame.sprite.Group,        damage, effect_status:dict=None, radius=None, duration_ms=None, color=None #explo
    #self, groups, pos, enemies:pygame.sprite.Group,        damage, effect_status:dict=None, radius=None, duration_ms=None, color=None) #linger
    #self, groups, pos, enemies:pygame.sprite.Group, enemy, damage, effect_status:dict=None,                                color=None #direct
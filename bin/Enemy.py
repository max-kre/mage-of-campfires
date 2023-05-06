import pygame
import math
from .settings import *
from .utils.utility_funcs import *

IMAGES = {
    "boss": pygame.image.load(f'data/graphics/enemies/boss.png'),
    "minion": pygame.image.load(f'data/graphics/enemies/minion.png')
}

class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, type, changePlayerGoldFunc, changePlayerHealthFunc, pos:pygame.math.Vector2=None,sounds=None) -> None:
        super().__init__(group)

        self.sounds = sounds

        self.type = type
        self.changePlayerGoldFunc = changePlayerGoldFunc
        self.changePlayerHealthFunc = changePlayerHealthFunc
        self.path = ENEMYPATH
        self.total_path_length = Enemy.getPathLength(self.path)
        self.pos = pos if pos is not None else pygame.math.Vector2(self.path[0])
        
        self.basestats = ENEMIES_BASEVALUES[type]
        print (self.type)
        # self.image = pygame.image.load(f'data/graphics/enemies/{self.type}.png')
        self.image = IMAGES[self.type].copy()
        self.rect = self.image.get_rect(midbottom=self.pos)

        #movement
        self.target_path_point = 1
        self.length_of_current_segment = Enemy.getPathLength([self.path[self.target_path_point-1],self.path[self.target_path_point]])
        self.combined_length_of_past_segments = 0
        self.percent_of_path_traveled = 0

        #live stats
        self.health = self.basestats["health"]
        self.worth = self.basestats["worth"]
        self.speed = self.basestats["speed"]
        self.penalty = self.basestats["penalty"]

        # flags n stuff
        self.got_hit = False
        self.is_alive = True

        #timers
        self.effect_timers = {
            "slow": effect_timer()
        }

    @staticmethod
    def getPathLength(path):
        path_length = 0
        for point_nr in range(len(path)-1):
            path_length += math.sqrt(
                (path[point_nr+1][0] - path[point_nr][0])**2 +
                (path[point_nr+1][1] - path[point_nr][1])**2
            )
        return path_length
    
    # def draw(self):
    #     pass
    
    def changeHealth(self,amount):
        if not self.is_alive:
            return
        self.health += amount
        self.got_hit = True if amount < 0 else False
        if self.sounds:
            self.sounds["hit_sound"].play()
        if self.health <= 0:
            self.enemyGotKilled()
        elif self.got_hit:
            self.got_hit_time = pygame.time.get_ticks()

    # def blink(self):
    #     blink_rate = 60
    #     now_tick = pygame.time.get_ticks()
    #     alpha = 255*(1+sin(now_tick/blink_rate))
    #     self.image.set_alpha(alpha)

    def update(self,dt):
        #_perc = self.health/self.basestats["health"]
        if self.got_hit:
           self.image.set_alpha(50)
           if (self.got_hit_time + CD_GOTHIT) < pygame.time.get_ticks():
               self.got_hit = False
               self.image.set_alpha(255)
        #else:
        #    self.image.fill((255*_perc,255*(1-_perc),0))
        self.move(dt)
        self.checkTimers()
        
        # print(self.pos.x, self.pos.y)

    def move(self,dt):
        dx = self.path[self.target_path_point][0] - self.pos.x
        dy = self.path[self.target_path_point][1] - self.pos.y
        direction = pygame.math.Vector2((dx,dy))
        direction = direction.normalize()
        self.pos.x += direction.x * self.speed * dt
        self.pos.y += direction.y * self.speed * dt
        
        #check if next checkpoint has been passed
        distance_to_last_point = Enemy.getPathLength([self.path[self.target_path_point-1],self.pos])
        self.percent_of_path_traveled = (self.combined_length_of_past_segments + distance_to_last_point) / self.total_path_length
        if distance_to_last_point>=self.length_of_current_segment:
            self.combined_length_of_past_segments += self.length_of_current_segment
            self.target_path_point += 1
            if self.target_path_point >= len(self.path):
                self.enemyGotThrough()
                return
            self.length_of_current_segment = Enemy.getPathLength([self.path[self.target_path_point-1],self.path[self.target_path_point]])
        
        #move rect to current pos
        self.rect.midbottom = self.pos

    def checkTimers(self):
        gameticks_now = pygame.time.get_ticks()
        for effect,timer in zip(self.effect_timers.keys(),self.effect_timers.values()):
            if timer.is_active:
                timer.update(gameticks_now)
                if timer.has_just_finished:
                    self.handleEffects(effect,start=False)
                    timer.reset()

    def handleEffects(self,effect_type:str,start=True,info_dict:dict=None):
        if effect_type == "slow":
            if start:
                self.effect_timers["slow"].start_timer(pygame.time.get_ticks(),info_dict["duration_sec"])
                self.speed = self.basestats["speed"] * info_dict["slow_percent"]/100
            else:
                self.speed = self.basestats["speed"]


    def enemyGotThrough(self):
        print('Got through!')
        self.changePlayerHealthFunc(-self.penalty)
        self.kill()

    def enemyGotKilled(self):
        self.is_alive = False
        print("BLARGH")
        if self.sounds:
            self.sounds["death_sound"].play()
        self.changePlayerGoldFunc(self.worth)
        self.kill()


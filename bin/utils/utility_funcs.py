import pygame
import math
# from .Enemy import Enemy

def enemyInRange(pos1:pygame.math.Vector2,pos2:pygame.math.Vector2,radius:float):
    if math.sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2) <= radius:
        return True
    else:
        return False
    

def calcLengthBetweenPos(pos1:pygame.math.Vector2,pos2:pygame.math.Vector2):
    return math.sqrt((pos2.x - pos1.x)**2 +(pos2.y - pos1.y)**2)


class effect_timer:
    def __init__(self) -> None:
        self.reset()
        
    def update(self, gameticks_now):
        if self.has_just_finished:
            return
        if gameticks_now > self.starttime + self.duration_sec:
            #duration over
            self.has_just_finished = True

    def start_timer(self, gameticks_now, duration_sec):
        self.starttime = gameticks_now
        self.duration_sec = duration_sec
        self.is_active = True

    def reset(self):
        self.duration_sec = 0
        self.starttime = 0
        self.is_active = False
        self.has_just_finished = False

import pygame
import math
# from .Enemy import Enemy

def enemyInRange(pos1:pygame.math.Vector2,pos2:pygame.math.Vector2,radius:float):
    if math.sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2) <= radius:
        return True
    else:
        return False
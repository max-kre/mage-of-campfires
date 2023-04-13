import pygame
import math
from settings import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, group, pos:pygame.math.Vector2) -> None:
        super().__init__(group)

        self.name = ""
        self.pos = pos
        self.image = pygame.Surface((64,64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=self.pos)

        self.health = 1
        self.worth = 1
        self.speed = 400

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

    def update(self,dt):
        pass
        
        # print(self.pos.x, self.pos.y)


    def enemyGotThrough(self):
        print('Got through!')
        self.kill()
        del self


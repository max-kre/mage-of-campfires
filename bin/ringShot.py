import pygame
import pygame.gfxdraw

class RingShotSprite(pygame.sprite.Sprite):
    def __init__(self, groups, pos, radius=None, color=None) -> None:
        super().__init__(groups)
        
        self.pos = pos
        print(pos)
        self.color = color if color else (255,50,50)
        self.init_time = pygame.time.get_ticks()
        self.animation_time = 200 #ms
        self.max_radius = radius if radius else 25
        self.image = pygame.Surface([self.max_radius*2, self.max_radius*2],pygame.SRCALPHA)
        # self.image.fill("white")
        # self.image.set_colorkey("white")
        self.rect = self.image.get_rect(center=self.pos)

    def update(self,dt):
        scaling_factor = (pygame.time.get_ticks() - self.init_time) / self.animation_time
        if scaling_factor > 1:
            self.kill()
            return
        self.image = pygame.Surface([self.max_radius*2, self.max_radius*2],pygame.SRCALPHA)
        r = int(scaling_factor * self.max_radius)
        pygame.gfxdraw.circle(self.image,self.max_radius,self.max_radius,r,self.color)
        # pygame.gfxdraw.filled_circle(self.image,self.max_radius,self.max_radius,r,(123,20,20))
        # self.image.set_alpha(125)
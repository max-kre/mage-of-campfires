import pygame
from sys import exit
from pygame import mixer
from settings import *
from Enemy import Enemy

class Game:
    def __init__(self) -> None:
        #only for __main__ reasons!
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE) 
        
        
        self.run_game = True
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.get_surface()
        print((self.display_surface.get_width(),self.display_surface.get_height()))
        self.bg_img = pygame.Surface((self.display_surface.get_width(),self.display_surface.get_height()))
        self.bg_img.fill('black')
        #start BG music
        # mixer.init()
        # mixer.music.load('data/Audio/spooky.wav')
        # mixer.music.play(-1)
        
        self.lives = STARTLIVES
        self.gold = STARTGOLD
        self.enemies = []
        self.towers = []
        self.all_sprite_objects = pygame.sprite.Group()

    def run(self):
        self.spawnEnemy()
        self.starttime=pygame.time.get_ticks()
        self.isReady = False
        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("I wanna quit")
                    #print(self.enemies[0].speed)
                    self.run_game = False
                    pygame.quit()
                    exit()
            dt = self.clock.tick() / 1000
            self.update(dt)
            self.draw()
            pygame.display.update()
        pass

    def spawnEnemy(self):
        self.enemies.append(Enemy(group=self.all_sprite_objects, type='boss', changePlayerGoldFunc=self.changeGold, changePlayerHealthFunc=self.changeLife))
        self.enemies.append(Enemy(group=self.all_sprite_objects, type='minion', changePlayerGoldFunc=self.changeGold, changePlayerHealthFunc=self.changeLife))
        # Enemy(group=self.all_sprite_objects,type='minion')
        # self.enemies.append(Enemy(pos=pygame.math.Vector2((0,100)), group=self.all_sprite_objects))

    def changeLife(self,amount):
        self.lives += amount

    def changeGold(self,amount):
        self.gold += amount

    def update(self,dt):
        # for e in self.enemies:
        #     e.update()
        if pygame.time.get_ticks() > self.starttime + 200:
            self.isReady=True
        if self.isReady:
            for e in self.enemies:
                e.changeHealth(-1)
            self.isReady=False
            self.starttime = pygame.time.get_ticks()
        pass
        self.all_sprite_objects.update(dt)

    def draw(self):
        # draw bg
        # self.screen.fill("red")
        self.display_surface.blit(self.bg_img,(0,0))
        self.all_sprite_objects.draw(self.display_surface)

if __name__ == "__main__":
    game = Game()
    game.run()

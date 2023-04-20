import pygame
from sys import exit
from pygame import mixer
from .settings import *
from .Enemy import Enemy
from .Tower import Tower

class Game:
    def __init__(self) -> None:
        #only for __main__ reasons!
        pygame.init()
        # self.screen = pygame.display.set_mode(SCREENSIZE) 
        self.sounds = {
            "hit_sound": pygame.mixer.Sound("./data/audio/Dumpster Door Hit.mp3"),
            "death_sound": pygame.mixer.Sound("./data/audio/Wooden Bat Hits Baseball Run.mp3")
        }
        self.sounds["hit_sound"].set_volume(0.01)
        self.sounds["death_sound"].set_volume(0.1)
        
        self.run_game = True
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.get_surface()
        print((self.display_surface.get_width(),self.display_surface.get_height()))
        self.bg_img = pygame.image.load('data/graphics/bg.png')
        self.ui_font_40px = pygame.font.Font(None, 40)
        #start BG music
        # mixer.init()
        # mixer.music.load('data/Audio/spooky.wav')
        # mixer.music.play(-1)
        
        self.lives = STARTLIVES
        self.gold = STARTGOLD
        self.wave_counter = 0
        self.tower_sprites = pygame.sprite.Group()
        self.animation_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

    def run(self):
        self.spawnDummyTower()
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

    def spawnEnemyWave(self):
        if self.wave_counter % 5:
            Enemy(group=self.enemy_sprites, type='minion', changePlayerGoldFunc=self.changeGold, changePlayerHealthFunc=self.changeLife,sounds=self.sounds)
        else:
            Enemy(group=self.enemy_sprites, type='boss', changePlayerGoldFunc=self.changeGold, changePlayerHealthFunc=self.changeLife,sounds=self.sounds)
        # Enemy(group=self.enemy_sprites,type='minion')
        # self.enemies.append(Enemy(pos=pygame.math.Vector2((0,100)), group=self.enemy_sprites))
        
    def spawnDummyTower(self):
        Tower(self.tower_sprites,pygame.math.Vector2((430,387)),enemy_group=self.enemy_sprites, animation_group=self.animation_sprites, type="blast")
        # Tower(self.tower_sprites,pygame.math.Vector2((500,450)),enemy_group=self.enemy_sprites, animation_group=self.animation_sprites, type="sniper")

    def changeLife(self,amount):
        self.lives += amount
        print("Lives",self.lives)

    def changeGold(self,amount):
        self.gold += amount
        print("Gold",self.gold)

    def update(self,dt):
        if pygame.time.get_ticks() > self.starttime + 500:
            self.isReady=True
        if self.isReady:
            self.spawnEnemyWave()
            self.wave_counter += 1
            print("RAWR", self.wave_counter)
            self.isReady=False
            self.starttime = pygame.time.get_ticks()
        pass
        self.enemy_sprites.update(dt)
        self.tower_sprites.update(dt)
        self.animation_sprites.update(dt)

    def drawUI(self):
        gold_img = self.ui_font_40px.render(f"Gold: {self.gold}", False, "black")
        gold_rect = gold_img.get_rect(topright=(SCREENSIZE[0]-25,8))
        lives_img = self.ui_font_40px.render(f"Lives: {self.lives}", False, "red")
        lives_rect = lives_img.get_rect(topleft=(25,8))
        wave_img = self.ui_font_40px.render(f"Sent: {self.wave_counter}", False, "black")
        wave_rect = wave_img.get_rect(midtop=(SCREENSIZE[0]//2,15))
        self.display_surface.blit(gold_img, gold_rect)
        self.display_surface.blit(lives_img, lives_rect)
        self.display_surface.blit(wave_img, wave_rect)
        pass

    def draw(self):
        # draw bg
        self.display_surface.blit(self.bg_img,(0,0))
        pygame.draw.aalines(self.display_surface,"white",False,ENEMYPATH,1)
        self.enemy_sprites.draw(self.display_surface)
        self.tower_sprites.draw(self.display_surface)
        self.animation_sprites.draw(self.display_surface)
        self.drawUI()

if __name__ == "__main__":
    game = Game()
    game.run()

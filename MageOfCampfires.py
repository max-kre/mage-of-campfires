import pygame
import os, sys
from pygame import mixer
from bin.settings import SCREENSIZE
from bin.main import Game
from bin.menu import MainMenu
# from bin.Enemy import Enemy
# from bin.Tower import Tower

# handle main UI with menu etc
# handle overall flow
class MoC_Main():
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(64)
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption('Mage of Campfires - Lit!')
        

        self.main_menu = MainMenu()
        self.game = Game()

        pygame.mouse.set_visible(True)
        
        pass
    #init vars

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("I wanna quit")
                    pygame.quit()
                    sys.exit()
            
            #start menu screen
            if self.main_menu.update() == True:
                self.main_menu.run()
                
            elif self.main_menu.update() == False:
                print("start game")
                self.game.run()

            else:
                pass
            

    #...
    #...

    #cleanup
    #handle exit


        pass



if __name__ == "__main__":
    menu = MoC_Main()
    menu.run()

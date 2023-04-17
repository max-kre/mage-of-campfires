import pygame
import os
from pygame import mixer
from bin.settings import SCREENSIZE
from bin.main import Game


# handle main UI with menu etc
# handle overall flow
class MoC_Main():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption('Mage of Campfires - Lit!')
        

        self.run_game = False
        self.game = Game()

        pygame.mouse.set_visible(False)
        
        pass
    #init vars

    def run(self):
    #start game in menu screen
        self.game.run()
    #...
    #...

    #cleanup
    #handle exit


        pass



if __name__ == "__main__":
    game = MoC_Main()
    game.run()

import unittest
from unittest.mock import MagicMock

import pygame
from bin import Tower 

class TowerTest(unittest.TestCase):
    
    def testTowersAttrs(self):
        for tower in Tower.__all__:
            checkAttrs = [
                "color",
                "range",
                "damage",
                "attackDelay",
                "targetStrategy",
                "effects",
                "pos",
                "height",
                "width",
                "base_image",
            ]
            for attr in checkAttrs:
                towerUnderTest = getattr(Tower, tower)(
                    pygame.sprite.Group(),
                    (430, 387),
                    pygame.sprite.Group(),
                    pygame.sprite.Group(),
                )
                self.assertTrue(hasattr(towerUnderTest, attr), f'Object {tower} has no attribute {attr}!')

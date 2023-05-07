#Settings for game

SCREENSIZE = (1200,800)


#damage to enemies
CD_GOTHIT = 100 # time in ms for enemy to blink after getting hit
COL_GOTHIT = (150,150,150)

#gameplay
STARTGOLD = 200
STARTLIVES = 10

#enemies
ENEMYPATH = [(0,137),(1020,137),(1072,164),(1072,248),(1020,300),(400,305),(343,351),(343,490),(446,546),(1054,551),(1121,592),(1121,695),(1060,735),(-20,745)]
ENEMIES_BASEVALUES = {
    "boss": {
        "health" : 500,
        "worth" : 10,
        "penalty": 5,
        "speed" : 150,
        "size" : 48
    },
    "minion": {
        "health" : 100,
        "worth" : 2,
        "penalty": 1,
        "speed" : 300,
        "size" : 32
    }
}


TOWER_BASEVALUES = {
    "blast": {
        "color" : (250,25,25),
        "range" : 300, #radius in px
        "damage" : 0,
        # "has_splash": True,
        #"splash_radius" : 250, #px
        "attack_delay" : 1200, #ms
        "target_strategy": "first",
        "effects": {
            "spawn_explosion":{
                "damage": 20,
                "radius": 250,
                "effect": #None
                    {
                    "create_puddle": {
                        "damage": 50,
                        "radius": 25,
                        "duration":500,
                        "effect": None
                    }
                }
            }
        }
    },
    "sniper": {
        "color": (50,50,50),
        "range" : 700,
        "damage" : 50,
        # "has_splash": False,
        "attack_delay" : 1000,
        "target_strategy": "strongest",
        "effects": None
    },
    "puddler": {
        "color": (25,250,50),
        "range" : 700,
        "damage" : 0,
        # "has_splash": False,
        "attack_delay" : 1000,
        "target_strategy": "first",
        "effects":{
            "create_puddle": {
                "damage": 50,
                "radius": 50,
                "effect": {
                    # "spawn_explosion":{
                    #     "damage": 2,
                    #     "radius": 150,
                    #     "effect": None
                    # },
                    "slow":{
                        "duration_sec": 0.5,
                        "slow_percent": 50
                    }
                }
            }
        }
    }
}
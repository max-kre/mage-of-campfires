#Settings for game

SCREENSIZE = (1200,800)


#damage to enemies
CD_GOTHIT = 70 # time in ms for enemy to blink after getting hit
COL_GOTHIT = (150,150,150)

#gameplay
STARTGOLD = 200
STARTLIVES = 10

#enemies
ENEMYPATH = [(0,137),(1020,137),(1072,164),(1072,248),(1020,300),(400,305),(343,351),(343,490),(446,546),(1054,551),(1121,592),(1121,695),(1060,735),(-20,745)]
ENEMIES_BASEVALUES = {
    "boss": {
        "health" : 200,
        "worth" : 10,
        "penalty": 5,
        "speed" : 150,
        "size" : 48
    },
    "minion": {
        "health" : 50,
        "worth" : 2,
        "penalty": 1,
        "speed" : 300,
        "size" : 32
    }
}


TOWER_BASEVALUES = {
    "blast": {
        "color" : (25,25,25),
        "range" : 300, #radius in px
        "damage" : 20,
        # "has_splash": True,
        "splash_radius" : 250, #px
        "attack_delay" : 1200, #ms
        "target_strategy": "first"
    },
    "sniper": {
        "color": (25,250,250),
        "range" : 700,
        "damage" : 50,
        # "has_splash": False,
        "attack_delay" : 500,
        "target_strategy": "first"
    }
}
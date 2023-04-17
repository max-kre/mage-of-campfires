#Settings for game

SCREENSIZE = (1200,800)


#damage to enemies
CD_GOTHIT = 70 # time in ms for enemy to blink after getting hit
COL_GOTHIT = (150,150,150)

#gameplay
STARTGOLD = 200
STARTLIVES = 10

#enemies
ENEMYPATH = [(-50,100),(1000,100),(1100,200),(1000,300),(-50,300)]
ENEMIES_BASEVALUES = {
    "boss": {
        "health" : 100,
        "worth" : 10,
        "penalty": 5,
        "speed" : 100,
        "size" : 48
    },
    "minion": {
        "health" : 10,
        "worth" : 2,
        "penalty": 1,
        "speed" : 400,
        "size" : 32
    }
}


TOWER_BASEVALUES = {
    "blast": {
        "color" : (25,25,25),
        "range" : 300, #radius in px
        "damage" : 5,
        # "has_splash": True,
        "splash_radius" : 250, #px
        "attack_delay" : 500, #ms
        "target_strategy": "first"
    },
    "sniper": {
        "color": (25,250,250),
        "range" : 700,
        "damage" : 30,
        # "has_splash": False,
        "attack_delay" : 1000,
        "target_strategy": "strongest"
    }
}
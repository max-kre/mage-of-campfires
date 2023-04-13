#Settings for game

SCREENSIZE = (1200,800)



#gameplay
STARTGOLD = 200
STARTLIVES = 10

#enemies
ENEMYPATH = [(-50,100),(1000,100),(1100,200),(1000,300),(-50,300)]
ENEMIES_BASEVALUES = {
    "boss": {
        "health" : 50,
        "worth" : 50,
        "penalty": 5,
        "speed" : 300,
        "size" : 64
    },
    "minion": {
        "health" : 3,
        "worth" : 2,
        "penalty": 1,
        "speed" : 400,
        "size" : 32
    }
}
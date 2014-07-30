'''
With this module you can save and load a game.
'''

###########
#LOAD GAME#
###########

def save(towers, m):
    import pickle
    import os
    if not os.path.exists("saves"):
        os.mkdir("saves")    
    save = open("saves\\save.txt", "wb")
    pickle.dump(towers, save)
    pickle.dump(m, save)
    save.close()
    print('Game saved !')

def load():        
    import pickle
    load = open("saves\\save.txt", "rb")
    towers = pickle.load(load)
    m = pickle.load(load)
    load.close()
    print('Game loaded !')





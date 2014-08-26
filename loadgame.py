'''
With this module you can save and load a game.
'''

import pickle
import os
    
def save(towers, m):
    if not os.path.exists("saves"):
        os.mkdir("saves")    
    save = open("saves\\save.txt", "wb")
    pickle.dump(towers, save)
    pickle.dump(m, save)
    save.close()
    print('Game saved !')

def load():        
    load = open("saves\\save.txt", "rb")
    global towers
    global m
    towers = pickle.load(load)
    m = pickle.load(load)
    load.close()
    print('Game loaded !')





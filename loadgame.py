'''
With this module you can load a saved game.
'''

###########
#LOAD GAME#
###########

print('\n', 'LOAD GAME', '\n')

load = open("D:\\python34\\test\\Towers of Hanoi\\saves\\saves.txt", "r")
load_read = load.read()
load_list = load_read.split('\n')

towers = load_list[0]
m = int(load_list[1])

load.close()





'''
With this module you can change the difficulty and tun a new game.
'''

##########
#NEW GAME#
##########

print('\n', 'NEW GAME', '\n'*2,
      '1. EASY \n',
      '2. NORMAL \n',
      '3. HARD \n',
      '4. EXPERT \n')

tower1 = [1, 2]
tower2 = []
tower3 = []

def difficulty(n):
    if n not in range(1, 4):
        print('Syntax Error ! Try Again')
    if n == 1:
        tower1 = [1, 2, 3, 4, 5]
    elif n == 2:
        tower1 = [1, 2, 3, 4, 5, 6, 7, 8]
    elif n == 3:
        tower1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elif n == 4:
        tower1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print("Tower 1 :", tower1)
    print("Tower 2 :", tower2)
    print("Tower 3 :", tower3)

def move(tower_source, tower_destination):
    if tower_source == 1 and tower_destination == 2:
        disc = tower1.pop(0)
        tower2.insert(0, disc)
    print("Tower 1 :", tower1)
    print("Tower 2 :", tower2)
    print("Tower 3 :", tower3)
        
    

    
    
    


